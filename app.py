import os
from datetime import datetime, timedelta

def configure_remote(repo_url):
    """Configures the remote if not already set."""
    remotes = os.popen('git remote').read()
    if 'origin' not in remotes:
        os.system(f'git remote add origin {repo_url}')

def make_commits():
    """Creates commits to spell 'HELLO' on the GitHub contribution calendar."""
    # Define the dates for the letters "HELLO"
    # Adjust these dates to fit your calendar
    dates = [
        # H
        "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05",
        "2025-01-03", "2025-02-03", "2025-03-03", "2025-04-03", "2025-05-03",
        "2025-01-05", "2025-02-05", "2025-03-05", "2025-04-05", "2025-05-05",
        # E
        "2025-01-07", "2025-01-08", "2025-01-09", "2025-01-10", "2025-01-11",
        "2025-01-07", "2025-02-07", "2025-03-07", "2025-04-07", "2025-05-07",
        "2025-01-09", "2025-02-09", "2025-03-09", "2025-04-09", "2025-05-09",
        # L
        "2025-01-12", "2025-01-13", "2025-01-14", "2025-01-15", "2025-01-16",
        "2025-01-12", "2025-02-12", "2025-03-12", "2025-04-12", "2025-05-12",
        # L
        "2025-01-17", "2025-01-18", "2025-01-19", "2025-01-20", "2025-01-21",
        "2025-01-17", "2025-02-17", "2025-03-17", "2025-04-17", "2025-05-17",
        # O
        "2025-01-22", "2025-01-23", "2025-01-24", "2025-01-25", "2025-01-26",
        "2025-01-22", "2025-02-22", "2025-03-22", "2025-04-22", "2025-05-22",
        "2025-01-26", "2025-02-26", "2025-03-26", "2025-04-26", "2025-05-26",
    ]

    for date in dates:
        commit_date = datetime.strptime(date, "%Y-%m-%d")
        date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        os.environ["GIT_AUTHOR_DATE"] = date_str
        os.environ["GIT_COMMITTER_DATE"] = date_str
        with open('file.txt', 'a') as file:
            file.write(f'Commit on {date}\n')
        os.system('git add .')
        os.system(f'git commit -m "Commit on {date}"')

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
