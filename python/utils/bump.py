import argparse, re, sys
from pathlib import Path
from types import SimpleNamespace as sn

from .lib import data, log, toml

paths = sn(root=Path(__file__).parent.parent)
paths.pyproject = paths.root / 'pyproject.toml'
paths.readme = paths.root / 'docs/README.md'
paths.util_msgs = paths.root / 'utils/data/messages.json'

msgs = sn(**{ key:val['message'] for key,val in data.json.read(paths.util_msgs)['bump'].items() })

def parse_args():
    argp = argparse.ArgumentParser(description=msgs.app_DESC, add_help=False)
    argp.add_argument('-M', '--major', action='store_true', help=msgs.help_MAJOR)
    argp.add_argument('-m', '--minor', action='store_true', help=msgs.help_MINOR)
    argp.add_argument('-p', '--patch', action='store_true', help=msgs.help_PATCH)
    argp.add_argument('-n', '--no-commit', '--skip-commit', action='store_true', help=msgs.help_NO_COMMIT)
    argp.add_argument('-N', '--no-push', '--skip-push', action='store_true', help=msgs.help_NO_PUSH)
    argp.add_argument('-h', '--help', action='help', help=msgs.help_HELP)
    return argp.parse_args()

def init_vers(project, bump_type):
    prev_ver = project.version
    major, minor, patch = map(int, prev_ver.split('.'))
    if   bump_type == 'major' : patch = 0 ; minor = 0 ; major += 1
    elif bump_type == 'minor' : patch = 0 ; minor += 1
    elif bump_type == 'patch' : patch += 1
    new_ver = f'{major}.{minor}.{patch}'
    return prev_ver, new_ver

def bump_pyproject_vers(pyproject, project, new_ver):

    # Bump project.version
    pyproject['project']['version'] = new_ver
    toml.write(paths.pyproject, pyproject)
    log.success(msgs.log_BUMPED_PROJECT_VER.format(prev_ver=project.version, **locals()))

    # Bump project.urls['Releases']
    new_ver_tag = f'{project.name}-{new_ver}'
    changelog_url = f"{project.urls['Releases']}/tag/{new_ver_tag}"
    log.info(f'{msgs.log_UPDATING_CLOG_URL_IN} pyproject.toml...')
    pyproject['project']['urls']['Changelog'] = changelog_url
    toml.write(paths.pyproject, pyproject)
    log.success(msgs.log_BUMPED_CLOG_URL_VER_TAG.format(**locals()))

def update_readme_vers(new_ver):
    log.info(f'{msgs.log_UPDATING_VERS_IN} docs/README.md...')
    updated_readme_content = re.sub(
        r'([-v])\d{1,3}\.\d{1,3}\.\d{1,3}',  # match - or v + version
        lambda m: f'{m.group(1)}{new_ver}',  # safe replacement
        data.file.read(paths.readme)
    )
    data.file.write(paths.readme, updated_readme_content)
    log.success(msgs.log_UPDATED_README_VERS.format(**locals()))

def main():

    # Parse args
    args = parse_args()
    bump_type = 'major' if args.major else 'minor' if args.minor else 'patch' if args.patch else None
    if not bump_type:
        log.error(msgs.err_MISSING_BUMP_TYPE_ARG)
        sys.exit(1)

    # Init project data
    log.info(f'{msgs.log_LOADING_PYPROJECT.format(pyproject_path=paths.pyproject)}...')
    pyproject = toml.read(paths.pyproject)
    project = sn(**pyproject['project'])

    # Update files
    _, new_ver = init_vers(project, bump_type)
    bump_pyproject_vers(pyproject, project, new_ver)
    update_readme_vers(new_ver)

    # Git commit/push
    if args.no_commit:
        print(f'\n{msgs.log_SKIPPING_GIT_COMMIT}...')
    else:
        from .lib import git
        git.init_kudo_sync_bot(msgs)
        log.info(f'{msgs.log_COMMITTING_CHANGES}...')
        git.commit([str(paths.pyproject), str(paths.readme)],
            f'Bumped {project.name} versions to {new_ver}', '-n')
        if args.no_push:
            print(f'\n{msgs.log_SKIPPING_GIT_PUSH}...')
        else:
            log.info(f'{msgs.log_PUSHING_CHANGES}...')
            git.push()
            log.success(f'{msgs.log_PUSHED_ALL_COMMITS}')
        git.restore_og_config(msgs)

    log.success(f'{msgs.log_SUCCESS}! {project.name} {msgs.log_BUMPED_TO} v{new_ver}!')

if __name__ == '__main__' : main()
