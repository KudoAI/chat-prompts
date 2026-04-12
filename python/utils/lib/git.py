from pathlib import Path
import subprocess

BACKUP_PATH = Path.home() / '.gitconfig.backup'

def commit(files, msg, *args) : run('add', *files) ; run('commit', '-m', msg, *args)

def init_kudo_sync_bot(msgs):
    import os
    print(f'\n{msgs.log_SWITCHING_TO_KUDO_SYNC_BOT}...\n')
    KEY_ID = None
    gpg_keys_path = os.environ.get('GPG_KEYS_PATH')
    if gpg_keys_path:
        key_path = Path(gpg_keys_path) / 'kudo-sync-bot-private-key.asc'
        if key_path.exists() : subprocess.run(['gpg', '--batch', '--import', str(key_path)], check=True)
        key_id_path = Path(gpg_keys_path) / 'kudo-sync-bot-key-id.txt'
        if key_id_path.exists() : KEY_ID = key_id_path.read_text().strip()
    if KEY_ID : os.environ['GIT_COMMITTER_SIGNINGKEY'] = KEY_ID
    os.environ['GIT_AUTHOR_NAME'] = 'kudo-sync-bot'
    os.environ['GIT_AUTHOR_EMAIL'] = 'auto-sync@kudoai.com'
    os.environ['GIT_COMMITTER_NAME'] = 'kudo-sync-bot'
    os.environ['GIT_COMMITTER_EMAIL'] = 'auto-sync@kudoai.com'
    return True

def push() : run('push')

def run(*args):
    result = subprocess.run(['git'] + list(args), capture_output=True, text=True)
    if result.returncode != 0:
        import sys
        print(f"Git command failed: {' '.join(['git'] + list(args))}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()
