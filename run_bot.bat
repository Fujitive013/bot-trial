@echo off
REM Windows Batch Script to run the GitHub Commit Bot as a background service

echo Starting GitHub Commit Bot...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Install dependencies if needed
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

REM Check if git is configured
git config user.name >nul 2>&1
if errorlevel 1 (
    echo WARNING: Git user.name not configured
    echo Run: python auto_commit_bot.py --setup
)

git config user.email >nul 2>&1
if errorlevel 1 (
    echo WARNING: Git user.email not configured
    echo Run: python auto_commit_bot.py --setup
)

echo.
echo Choose an option:
echo 1. Setup configuration
echo 2. Make a manual commit
echo 3. Run as daemon (background service)
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    python auto_commit_bot.py --setup
) else if "%choice%"=="2" (
    python auto_commit_bot.py --commit
) else if "%choice%"=="3" (
    echo Starting daemon mode...
    echo Press Ctrl+C to stop the bot
    python auto_commit_bot.py --daemon
) else if "%choice%"=="4" (
    echo Goodbye!
) else (
    echo Invalid choice
)

pause
