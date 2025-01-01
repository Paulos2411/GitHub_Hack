import os
import random
from datetime import datetime, timedelta

def configure_git_repo(repo_url):
    """Initialize git repository and configure remote if needed."""
    # Check if .git directory exists, if not initialize
    if not os.path.exists('.git'):
        print("Initializing git repository...")
        os.system('git init')
        
    # Configure git user (you should replace with your actual email)
    os.system('git config user.name "Paulos2411"')
    os.system('git config user.email "paul.ortulidispflanz@gmail.com"')
    
    # Configure remote
    remotes = os.popen('git remote').read()
    if 'origin' not in remotes:
        print("Adding remote origin...")
        os.system(f'git remote add origin {repo_url}')

def make_commits():
    """Creates multiple commits per day from January 1, 2025 to October 31, 2025."""
    # Calculate date range: from January 1, 2025 to October 31, 2025
    start_date = datetime(2025, 1, 1).date()   # January 1, 2025
    end_date = datetime(2025, 10, 31).date()   # October 31, 2025
    
    print(f"Creating commits from {start_date} to {end_date}")
    
    # Generate dates for the range
    current_date = start_date
    commit_count = 0
    
    while current_date <= end_date:
        # Randomly decide commits for this day to look natural
        random_choice = random.random()
        
        if random_choice < 0.15:  # 15% chance - no commits (weekend/lazy day)
            daily_commits = 0
        elif random_choice < 0.40:  # 25% chance - light activity
            daily_commits = random.randint(1, 2)
        elif random_choice < 0.70:  # 30% chance - normal activity  
            daily_commits = random.randint(3, 5)
        else:  # 30% chance - heavy activity
            daily_commits = random.randint(6, 10)
        
        for commit_num in range(daily_commits):
            # Vary the time throughout the day
            hour = (commit_num * 2 + 8) % 24  # Spread commits throughout the day
            minute = (commit_num * 13) % 60
            second = (commit_num * 7) % 60
            
            commit_datetime = datetime.combine(current_date, datetime.min.time()) + timedelta(
                hours=hour, minutes=minute, seconds=second
            )
            
            date_str = commit_datetime.strftime("%Y-%m-%d %H:%M:%S")
            os.environ["GIT_AUTHOR_DATE"] = date_str
            os.environ["GIT_COMMITTER_DATE"] = date_str
            
            with open('file.txt', 'a') as file:
                file.write(f'Commit #{commit_count + 1} on {current_date} at {hour:02d}:{minute:02d}:{second:02d}\n')
            
            os.system('git add .')
            os.system(f'git commit -m "Commit #{commit_count + 1} on {current_date}"')
            commit_count += 1
            
            # Print progress
            if commit_count % 100 == 0:
                print(f"Created {commit_count} commits so far...")
        
        current_date += timedelta(days=1)
    
    print(f"Total commits created: {commit_count}")

def main():
    REPO_URL = 'https://github.com/Paulos2411/GitHub_Hack'
    
    # Configure Git repository and remote
    configure_git_repo(REPO_URL)

    # Make commits
    make_commits()

    # Force push commits to the remote (this will overwrite the remote repository)
    print("Force pushing all commits to remote repository...")
    os.system('git push --force-with-lease origin main')

if __name__ == '__main__':
    main()
