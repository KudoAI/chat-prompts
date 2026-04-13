#!/bin/bash

# Init UI colors
NC="\033[0m"    # no color
BR="\033[1;91m" # bright red
BY="\033[1;33m" # bright yellow
BG="\033[1;92m" # bright green
BW="\033[1;97m" # bright white

# Determine new version to bump to
BUMP_TYPES=("major" "minor" "patch")
old_ver=$(node -pe "require('./package.json').version")
IFS='.' read -ra subvers <<< "$old_ver" # split old_ver into subvers array
case $1 in
    "patch") subvers[2]=$((subvers[2] +1)) ;;
    "minor") subvers[1]=$((subvers[1] +1)) ; subvers[2]=0 ;;
    "major") subvers[0]=$((subvers[0] +1)) ; subvers[1]=0 ; subvers[2]=0 ;;
    *) echo -e "\n${BR}Invalid bump type arg provided: $1${NC}" ;
       echo -e "\n${BY}Valid args are: ${BUMP_TYPES[*]/#/--}${NC}" ;
       exit 1 ;;
esac
new_ver=$(printf "%s.%s.%s" "${subvers[@]}")

echo -e "${BY}Pulling latest changes from remote to sync local repository...${NC}\n"
git pull || (echo -e "${BR}Merge failed, please resolve conflicts!${NC}" && exit 1)
echo ''

echo -e "${BY}Bumping versions in package manifests...${BW}"
npm version --no-git-tag-version "$new_ver"

echo "Bumping versions in READMEs..."
find . -name 'README.md' -exec sed -i -E \
    "s/([-v])([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})/\1$new_ver/g" {} +
echo "v$new_ver"

echo -e "${BY}\nChanging Git author/committer to kudo-sync-bot...\n${NC}"
if [ -n "$GPG_KEYS_PATH" ] ; then
    KEY_PATH="$GPG_KEYS_PATH/kudo-sync-bot-private-key.asc"
    if [ -f "$KEY_PATH" ] ; then gpg --batch --import "$KEY_PATH" ; fi
    KEY_ID_PATH="$GPG_KEYS_PATH/kudo-sync-bot-key-id.txt"
    if [ -f "$KEY_ID_PATH" ] ; then KEY_ID="$(cat "$KEY_ID_PATH")" ; fi
fi
export GIT_AUTHOR_NAME="kudo-sync-bot"
export GIT_AUTHOR_EMAIL="auto-sync@kudoai.com"
export GIT_COMMITTER_NAME="kudo-sync-bot"
export GIT_COMMITTER_EMAIL="auto-sync@kudoai.com"

echo -e "${BY}\nCommitting bumps to Git...\n${NC}"
find . -name "README.md" -exec git add {} +
git add package*.json
git commit -n -m "Bumped $pkg_name versions to $new_ver" -S $KEY_ID

echo -e "${BY}\nPushing to GitHub...\n${NC}"
git push

echo -e "${BG}\nSuccessfully bumped to v$new_ver!${NC}"
