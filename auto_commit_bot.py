#!/usr/bin/env python3
"""
Automated GitHub Commit Bot
Creates regular commits to maintain green activity on GitHub profile
"""

import os
import random
import datetime
import subprocess
import json
import time
import schedule
from pathlib import Path


class GitHubCommitBot:
    def __init__(self, repo_path=None, config_file="config.json"):
        self.repo_path = repo_path or os.getcwd()
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from JSON file"""
        default_config = {
            "commit_messages": [
                "📝 Update daily log",
                "🔧 Minor improvements",
                "📊 Update statistics",
                "🎯 Daily progress",
                "✨ Small enhancements",
                "📈 Performance tweaks",
                "🔄 Regular maintenance",
                "📋 Update documentation",
                "🎨 Code cleanup",
                "🚀 Optimize workflow"
            ],
            "file_types": [
                "daily_log.md",
                "progress.txt",
                "notes.md",
                "stats.json",
                "activity.log"
            ],
            "schedule_times": ["09:00", "15:30", "21:00"],
            "weekend_activity": True,
            "commit_frequency": "daily",  # daily, twice_daily, random
            "github_username": "",
            "github_email": ""
        }

        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
            except Exception as e:
                print(f"Error loading config: {e}")
                return default_config
        else:
            # Create default config file
            with open(self.config_file, 'w') as f:
                json.dump(default_config, f, indent=4)
            print(f"Created default config file: {self.config_file}")
            return default_config

    def setup_git_config(self):
        """Setup git configuration"""
        if self.config.get("github_username") and self.config.get("github_email"):
            try:
                subprocess.run(["git", "config", "user.name", self.config["github_username"]],
                               cwd=self.repo_path, check=True)
                subprocess.run(["git", "config", "user.email", self.config["github_email"]],
                               cwd=self.repo_path, check=True)
                print("✅ Git configuration updated")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error setting git config: {e}")
        else:
            print("⚠️  Please update github_username and github_email in config.json")

    def create_or_update_file(self):
        """Create or update a file with meaningful content"""
        filename = random.choice(self.config["file_types"])
        filepath = os.path.join(self.repo_path, filename)

        content = self.generate_content(filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return filename

    def generate_content(self, filename):
        """Generate meaningful content based on file type"""
        now = datetime.datetime.now()

        if filename.endswith('.md'):
            return f"""# Daily Activity Log

Date: {now.strftime('%Y-%m-%d')}
Time: {now.strftime('%H:%M:%S')}

## Today's Activities
- Automated commit generation
- Code maintenance and updates
- Project organization

## Statistics
- Commits made: {random.randint(1, 10)}
- Files updated: {random.randint(1, 5)}
- Lines of code: {random.randint(50, 200)}

## Notes
{random.choice([
                "Focus on code quality and consistency",
                "Implementing best practices",
                "Regular maintenance and updates",
                "Improving project structure",
                "Optimizing development workflow"
            ])}

---
*Last updated: {now.isoformat()}*
"""

        elif filename.endswith('.json'):
            return json.dumps({
                "timestamp": now.isoformat(),
                "date": now.strftime('%Y-%m-%d'),
                "commits_today": random.randint(1, 5),
                "lines_added": random.randint(10, 100),
                "files_modified": random.randint(1, 8),
                "activity_score": random.randint(70, 100),
                "last_commit": now.strftime('%H:%M:%S')
            }, indent=2)

        elif filename.endswith('.log'):
            return f"""[{now.strftime('%Y-%m-%d %H:%M:%S')}] INFO: Daily activity logged
[{now.strftime('%Y-%m-%d %H:%M:%S')}] INFO: Automated commit process started
[{now.strftime('%Y-%m-%d %H:%M:%S')}] INFO: File updates completed
[{now.strftime('%Y-%m-%d %H:%M:%S')}] INFO: Git operations successful
[{now.strftime('%Y-%m-%d %H:%M:%S')}] INFO: Activity score: {random.randint(80, 100)}%
"""

        else:  # .txt files
            return f"""Daily Progress Report
===================

Date: {now.strftime('%A, %B %d, %Y')}
Time: {now.strftime('%I:%M %p')}

Activities Completed:
- Code review and optimization
- Documentation updates
- Project maintenance
- Automated workflows

Random Quote: "{random.choice([
                'Code is poetry written in logic.',
                'Every expert was once a beginner.',
                'Progress, not perfection.',
                'Consistency beats intensity.',
                'Small steps lead to big changes.'
            ])}"

Activity Level: {random.choice(['High', 'Medium', 'Steady'])}
Focus Area: {random.choice(['Development', 'Documentation', 'Testing', 'Optimization'])}

Next Steps:
- Continue regular development
- Maintain coding standards
- Update documentation as needed

---
Generated at: {now.isoformat()}
"""

    def make_commit(self):
        """Create a commit with updated files"""
        try:
            # Check if we're in a git repository
            result = subprocess.run(["git", "status"], cwd=self.repo_path,
                                    capture_output=True, text=True)
            if result.returncode != 0:
                print("❌ Not a git repository. Initializing...")
                subprocess.run(["git", "init"], cwd=self.repo_path, check=True)
                print("✅ Git repository initialized")

            # Create or update files
            updated_files = []
            num_files = random.randint(1, 2)  # Update 1-2 files per commit

            for _ in range(num_files):
                filename = self.create_or_update_file()
                updated_files.append(filename)

            # Add files to git
            for filename in updated_files:
                subprocess.run(["git", "add", filename],
                               cwd=self.repo_path, check=True)

            # Create commit
            commit_message = random.choice(self.config["commit_messages"])
            if len(updated_files) > 1:
                commit_message += f" ({', '.join(updated_files)})"

            subprocess.run(["git", "commit", "-m", commit_message],
                           cwd=self.repo_path, check=True)

            print(f"✅ Commit created: {commit_message}")
            return True

        except subprocess.CalledProcessError as e:
            print(f"❌ Error making commit: {e}")
            return False

    def push_commits(self):
        """Push commits to remote repository"""
        try:
            result = subprocess.run(["git", "push"], cwd=self.repo_path,
                                    capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Commits pushed to remote repository")
                return True
            else:
                print(f"⚠️  Push failed: {result.stderr}")
                return False
        except subprocess.CalledProcessError as e:
            print(f"❌ Error pushing commits: {e}")
            return False

    def should_commit_today(self):
        """Determine if we should commit today based on schedule"""
        today = datetime.datetime.now()

        # Check if weekend activity is disabled
        if not self.config.get("weekend_activity", True) and today.weekday() >= 5:
            return False

        return True

    def run_scheduled_commit(self):
        """Run a scheduled commit"""
        if not self.should_commit_today():
            print("⏭️  Skipping commit (weekend activity disabled)")
            return

        print(
            f"🤖 Running scheduled commit at {datetime.datetime.now().strftime('%H:%M:%S')}")

        if self.make_commit():
            # Optionally push commits (uncomment if you want auto-push)
            # self.push_commits()
            pass

    def setup_schedule(self):
        """Setup the commit schedule"""
        frequency = self.config.get("commit_frequency", "daily")

        if frequency == "daily":
            # One commit per day at a random time from schedule
            time_slot = random.choice(self.config["schedule_times"])
            schedule.every().day.at(time_slot).do(self.run_scheduled_commit)
            print(f"📅 Scheduled daily commits at {time_slot}")

        elif frequency == "twice_daily":
            # Two commits per day
            for time_slot in random.sample(self.config["schedule_times"], 2):
                schedule.every().day.at(time_slot).do(self.run_scheduled_commit)
                print(f"📅 Scheduled commits at {time_slot}")

        elif frequency == "random":
            # Random commits throughout the day
            for time_slot in self.config["schedule_times"]:
                # 60% chance of committing at each time slot
                if random.random() < 0.6:
                    schedule.every().day.at(time_slot).do(self.run_scheduled_commit)
                    print(f"📅 Scheduled random commit at {time_slot}")

    def run_daemon(self):
        """Run the bot as a daemon process"""
        print("🚀 Starting GitHub Commit Bot...")
        print(f"📂 Repository path: {self.repo_path}")

        self.setup_git_config()
        self.setup_schedule()

        print("⏰ Bot is running. Press Ctrl+C to stop.")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n🛑 Bot stopped by user")

    def manual_commit(self):
        """Make a manual commit right now"""
        print("🔧 Making manual commit...")
        if self.make_commit():
            push_choice = input("Push to remote? (y/n): ").lower().strip()
            if push_choice == 'y':
                self.push_commits()


def main():
    """Main function with CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(description="GitHub Commit Bot")
    parser.add_argument("--path", "-p", help="Repository path", default=".")
    parser.add_argument(
        "--config", "-c", help="Config file path", default="config.json")
    parser.add_argument(
        "--daemon", "-d", action="store_true", help="Run as daemon")
    parser.add_argument("--commit", action="store_true",
                        help="Make a manual commit")
    parser.add_argument("--setup", "-s", action="store_true",
                        help="Setup configuration")

    args = parser.parse_args()

    bot = GitHubCommitBot(args.path, args.config)

    if args.setup:
        # Interactive setup
        print("🔧 Setting up GitHub Commit Bot...")
        username = input("GitHub username: ").strip()
        email = input("GitHub email: ").strip()

        bot.config["github_username"] = username
        bot.config["github_email"] = email

        with open(bot.config_file, 'w') as f:
            json.dump(bot.config, f, indent=4)

        print("✅ Configuration saved!")

    elif args.commit:
        bot.manual_commit()

    elif args.daemon:
        bot.run_daemon()

    else:
        print("GitHub Commit Bot")
        print("Usage:")
        print("  python auto_commit_bot.py --setup     # Initial setup")
        print("  python auto_commit_bot.py --commit    # Manual commit")
        print("  python auto_commit_bot.py --daemon    # Run as daemon")


if __name__ == "__main__":
    main()
