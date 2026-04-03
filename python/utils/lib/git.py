from pathlib import Path
import subprocess

BACKUP_PATH = Path.home() / '.gitconfig.backup'

def commit(files, msg, *args) : run('add', *files) ; run('commit', '-m', msg, *args)

def init_kudo_sync_bot(msgs):
    import os
    print(f'\n{msgs.log_SWITCHING_TO_KUDO_SYNC_BOT}...\n')
    with open(BACKUP_PATH, 'w') as file: # back up git config
        file.write(run('config', '--global', '--list'))
    gpg_keys_path = os.environ.get('GPG_KEYS_PATH')
    if gpg_keys_path:
        key_path = Path(gpg_keys_path) / 'kudo-sync-bot-private-key.asc'
        if key_path.exists() : subprocess.run(['gpg', '--batch', '--import', str(key_path)], check=True)
        key_id_path = Path(gpg_keys_path) / 'kudo-sync-bot-key-id.txt'
        if key_id_path.exists():
            key_id = key_id_path.read_text().strip()
            run('config', '--global', 'user.signingkey', key_id)
    run('config', '--global', 'commit.gpgsign', 'true')
    run('config', '--global', 'user.name', 'kudo-sync-bot')
    run('config', '--global', 'user.email', 'auto-sync@kudoai.com')
    return True

def push() : run('push')

def restore_og_config(msgs):
    print(f'{msgs.log_RESTORING_OG_GIT_CONFIG}...')
    if BACKUP_PATH.exists():
        with open(BACKUP_PATH) as file:
            for line in file:
                if '=' in line:
                    key, val = line.strip().split('=', 1)
                    run('config', '--global', key, val)
        BACKUP_PATH.unlink()
    else:
        print(msgs.warn_GIT_CONFIG_BACKUP_NOT_FOUND)

def run(*args):
    result = subprocess.run(['git'] + list(args), capture_output=True, text=True)
    if result.returncode != 0:
        import sys
        print(f"Git command failed: {' '.join(['git'] + list(args))}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()
