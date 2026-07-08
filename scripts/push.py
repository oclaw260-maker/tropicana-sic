"""Push the tropicana-sic test page to GitHub Pages.

Uses the Python wrapper to avoid bash token-expansion pitfalls documented in
the github-pages-deploy skill.
"""
import os, subprocess, json, urllib.request

env = os.path.expanduser('~/.hermes/.env')
token = None
with open(env) as f:
    for line in f:
        if line.startswith('GITHUB_TOKEN='):
            token = line.strip().split('=', 1)[1]
            break
assert token, 'no GITHUB_TOKEN in ~/.hermes/.env'

USER = 'oclaw260-maker'
REPO = 'tropicana-sic'
WORK = '/home/turbo/tropicana-sic'

# 1. Stage + commit
subprocess.run(['git', '-C', WORK, 'add', '-A'], check=True)
result = subprocess.run(
    ['git', '-C', WORK, 'commit', '-m', 'Add README', '-q'],
    capture_output=True, text=True,
)
print('commit rc:', result.returncode, result.stdout, result.stderr[-200:])

# 2. Set remote with token
remote_url = f'https://{token}@github.com/{USER}/{REPO}.git'
subprocess.run(['git', '-C', WORK, 'remote', 'set-url', 'origin', remote_url], check=True)

# 3. Force push
result = subprocess.run(
    ['git', '-C', WORK, 'push', 'origin', 'main', '--force'],
    capture_output=True, text=True,
)
print('push rc:', result.returncode)
print('push stdout:', result.stdout[-300:])
print('push stderr:', result.stderr[-300:])
