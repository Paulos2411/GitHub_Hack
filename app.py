import os
from random import randint

def configure_remote(repo_url):
    """Configures the remote if not already set."""
    remotes = os.popen('git remote').read()
    if 'origin' not in remotes:
        os.system(f'git remote add origin {repo_url}')

def make_commits(num_days=365):
    """Creates random commits for a given number of days."""
    for i in range(1, num_days + 1):
        for _ in range(randint(1, 10)):
            date_str = f'{i} days ago'
            with open('file.txt', 'a') as file:
                file.write(date_str + '\n')
            os.system('git add .')
            os.system(f'git commit --date="{date_str}" -m "commit"')

def main():
    REPO_URL = 'https://github.com/Paulos2411/GitHub_Hack'
    
    # Configure Git remote
    configure_remote(REPO_URL)

    # Make commits
    make_commits()

    # Ensure the local branch is updated with any remote changes before pushing
    os.system('git pull origin main --rebase')
    
    # Push commits to the remote
    os.system('git push -u origin main')

if __name__ == '__main__':
    main()
