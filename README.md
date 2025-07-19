# GitHub Activity Bot

This repository contains automated scripts to maintain consistent GitHub activity through regular commits.

## 🤖 What it does

The bot automatically creates meaningful commits to your repository, helping maintain a "green" GitHub activity graph. It creates and updates various types of files (logs, documentation, statistics) with realistic content.

## 📁 Files

-   `auto_commit_bot.py` - Full-featured bot with scheduling
-   `simple_commit.py` - Lightweight single-commit script
-   `config.json` - Configuration file for the bot
-   `run_bot.bat` - Windows batch script to run the bot
-   `requirements.txt` - Python dependencies

## 🚀 Quick Start

### Option 1: Simple Single Commit

```bash
python simple_commit.py
```

### Option 2: Full Bot with Scheduling

1. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Setup configuration:**

    ```bash
    python auto_commit_bot.py --setup
    ```

3. **Make a manual commit:**

    ```bash
    python auto_commit_bot.py --commit
    ```

4. **Run as daemon (scheduled commits):**
    ```bash
    python auto_commit_bot.py --daemon
    ```

### Option 3: Windows Batch Script

Double-click `run_bot.bat` for an interactive menu.

## ⚙️ Configuration

Edit `config.json` to customize:

-   **commit_messages**: Array of possible commit messages
-   **file_types**: Types of files to create/update
-   **schedule_times**: When to make automatic commits
-   **commit_frequency**: "daily", "twice_daily", or "random"
-   **weekend_activity**: Whether to commit on weekends
-   **github_username**: Your GitHub username
-   **github_email**: Your GitHub email

## 📊 Features

### Automated Commits

-   Scheduled commits at configurable times
-   Random commit messages and content
-   Multiple file types (Markdown, JSON, logs, text)
-   Realistic activity patterns

### Content Generation

-   Daily logs with timestamps
-   Progress reports
-   Statistics in JSON format
-   Activity logs
-   Documentation updates

### Flexible Scheduling

-   Daily commits
-   Multiple commits per day
-   Random timing
-   Weekend activity control

## 🛠️ Advanced Usage

### Custom Repository Path

```bash
python auto_commit_bot.py --path /path/to/repo --daemon
```

### Custom Config File

```bash
python auto_commit_bot.py --config my_config.json --daemon
```

## 📝 Generated Content Examples

### Daily Log (Markdown)

```markdown
# Daily Activity Log

Date: 2025-01-15
Time: 14:30:22

## Today's Activities

-   Automated commit generation
-   Code maintenance and updates
-   Project organization

## Statistics

-   Commits made: 3
-   Files updated: 2
-   Lines of code: 127
```

### Statistics (JSON)

```json
{
    "timestamp": "2025-01-15T14:30:22.123456",
    "date": "2025-01-15",
    "commits_today": 2,
    "lines_added": 45,
    "files_modified": 3,
    "activity_score": 87
}
```

## 🔒 Security & Ethics

### Important Notes:

-   This tool is for maintaining legitimate activity on your own repositories
-   Generated commits contain meaningful content, not empty commits
-   All commits are real changes to actual files
-   Use responsibly and in accordance with your organization's policies

### Best Practices:

-   Use on personal repositories or with permission
-   Don't use to inflate contribution metrics unfairly
-   Review generated content periodically
-   Keep commit frequency realistic

## 🎯 Use Cases

-   **Maintaining Activity**: Keep your GitHub graph green during breaks
-   **Learning Projects**: Regular commits while studying/practicing
-   **Portfolio Maintenance**: Consistent activity for job applications
-   **Habit Building**: Develop consistent coding habits

## 📋 Requirements

-   Python 3.6+
-   Git installed and configured
-   GitHub repository (local or remote)
-   `schedule` library (installed via requirements.txt)

## 🔧 Troubleshooting

### Git Not Configured

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Repository Not Initialized

The script will automatically run `git init` if needed.

### Push Failures

Make sure your remote repository is configured:

```bash
git remote add origin https://github.com/username/repository.git
git branch -M main
git push -u origin main
```

## 📄 License

This project is provided as-is for educational and personal use. Use responsibly.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

_Remember to use this tool ethically and in accordance with GitHub's terms of service._
