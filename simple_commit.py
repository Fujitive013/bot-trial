#!/usr/bin/env python3
"""
Simple Auto Commit Script
A lightweight alternative to the full bot for quick setup
"""

import os
import random
import datetime
import subprocess
import json


def get_random_commit_message():
    """Get a random commit message"""
    messages = [
        "📝 Daily update",
        "🔧 Minor improvements",
        "📊 Update progress",
        "✨ Small enhancements",
        "📈 Performance tweaks",
        "🔄 Regular maintenance",
        "📋 Documentation update",
        "🎨 Code cleanup",
        "🚀 Workflow optimization",
        "💡 New insights"
    ]
    return random.choice(messages)


def create_activity_file():
    """Create or update an activity file"""
    now = datetime.datetime.now()

    # Create a simple activity log
    content = f"""# Activity Log

Last Updated: {now.strftime('%Y-%m-%d %H:%M:%S')}

## Recent Activity
- Automated commit on {now.strftime('%A, %B %d, %Y')}
- Time: {now.strftime('%I:%M %p')}
- Status: Active

## Statistics
- Total commits: {random.randint(50, 200)}
- Files updated: {random.randint(10, 50)}
- Last activity: {now.isoformat()}

---
*Auto-generated activity log*
"""

    with open('activity_log.md', 'w', encoding='utf-8') as f:
        f.write(content)

    return 'activity_log.md'


def make_commit():
    """Make a single commit"""
    try:
        # Check if git repo exists
        if not os.path.exists('.git'):
            print("Initializing git repository...")
            subprocess.run(['git', 'init'], check=True)

        # Create/update file
        filename = create_activity_file()
        print(f"Created/updated: {filename}")

        # Add to git
        subprocess.run(['git', 'add', filename], check=True)

        # Commit
        message = get_random_commit_message()
        subprocess.run(['git', 'commit', '-m', message], check=True)

        print(f"✅ Commit successful: {message}")

        # Ask about pushing
        push = input("Push to remote repository? (y/n): ").lower().strip()
        if push == 'y':
            try:
                subprocess.run(['git', 'push'], check=True)
                print("✅ Pushed to remote repository")
            except subprocess.CalledProcessError:
                print("⚠️ Push failed - make sure remote is configured")

        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    print("🤖 Simple Auto Commit Script")
    print("=" * 30)

    make_commit()
