# PowerShell script to run the GitHub Commit Bot

param(
    [string]$Action = "menu",
    [string]$Path = ".",
    [string]$Config = "config.json"
)

function Show-Menu {
    Write-Host "GitHub Commit Bot - PowerShell Edition" -ForegroundColor Green
    Write-Host "=====================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "1. Setup Configuration" -ForegroundColor Yellow
    Write-Host "2. Make Manual Commit" -ForegroundColor Yellow
    Write-Host "3. Run Simple Commit" -ForegroundColor Yellow
    Write-Host "4. Start Daemon Mode" -ForegroundColor Yellow
    Write-Host "5. Install Dependencies" -ForegroundColor Yellow
    Write-Host "6. Check Git Status" -ForegroundColor Yellow
    Write-Host "7. Exit" -ForegroundColor Yellow
    Write-Host ""
}

function Install-Dependencies {
    Write-Host "Installing Python dependencies..." -ForegroundColor Blue
    
    if (!(Test-Path "venv")) {
        Write-Host "Creating virtual environment..." -ForegroundColor Blue
        python -m venv venv
    }
    
    Write-Host "Activating virtual environment..." -ForegroundColor Blue
    & ".\venv\Scripts\Activate.ps1"
    
    Write-Host "Installing requirements..." -ForegroundColor Blue
    pip install -r requirements.txt
    
    Write-Host "Dependencies installed successfully!" -ForegroundColor Green
}

function Check-GitStatus {
    Write-Host "Checking Git configuration..." -ForegroundColor Blue
    
    try {
        $gitName = git config user.name
        $gitEmail = git config user.email
        
        if ($gitName) {
            Write-Host "Git user.name: $gitName" -ForegroundColor Green
        } else {
            Write-Host "Git user.name: NOT SET" -ForegroundColor Red
        }
        
        if ($gitEmail) {
            Write-Host "Git user.email: $gitEmail" -ForegroundColor Green
        } else {
            Write-Host "Git user.email: NOT SET" -ForegroundColor Red
        }
        
        $gitStatus = git status 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Git repository: INITIALIZED" -ForegroundColor Green
        } else {
            Write-Host "Git repository: NOT INITIALIZED" -ForegroundColor Red
        }
        
        $remotes = git remote 2>&1
        if ($remotes -and $LASTEXITCODE -eq 0) {
            Write-Host "Git remotes: $remotes" -ForegroundColor Green
        } else {
            Write-Host "Git remotes: NONE CONFIGURED" -ForegroundColor Yellow
        }
        
    } catch {
        Write-Host "Git is not installed or not in PATH" -ForegroundColor Red
    }
}

function Run-SimpleCommit {
    Write-Host "Running simple commit script..." -ForegroundColor Blue
    python simple_commit.py
}

function Run-Setup {
    Write-Host "Running bot setup..." -ForegroundColor Blue
    python auto_commit_bot.py --setup
}

function Run-ManualCommit {
    Write-Host "Making manual commit..." -ForegroundColor Blue
    python auto_commit_bot.py --commit
}

function Run-Daemon {
    Write-Host "Starting daemon mode..." -ForegroundColor Blue
    Write-Host "Press Ctrl+C to stop the bot" -ForegroundColor Yellow
    python auto_commit_bot.py --daemon
}

# Main execution
if ($Action -eq "menu") {
    do {
        Show-Menu
        $choice = Read-Host "Enter your choice (1-7)"
        
        switch ($choice) {
            "1" { Run-Setup }
            "2" { Run-ManualCommit }
            "3" { Run-SimpleCommit }
            "4" { Run-Daemon }
            "5" { Install-Dependencies }
            "6" { Check-GitStatus }
            "7" { 
                Write-Host "Goodbye!" -ForegroundColor Green
                exit 
            }
            default { 
                Write-Host "Invalid choice. Please enter 1-7." -ForegroundColor Red 
            }
        }
        
        if ($choice -ne "7") {
            Write-Host ""
            Read-Host "Press Enter to continue"
            Clear-Host
        }
    } while ($choice -ne "7")
} else {
    # Direct action execution
    switch ($Action.ToLower()) {
        "setup" { Run-Setup }
        "commit" { Run-ManualCommit }
        "simple" { Run-SimpleCommit }
        "daemon" { Run-Daemon }
        "install" { Install-Dependencies }
        "status" { Check-GitStatus }
        default { 
            Write-Host "Unknown action: $Action" -ForegroundColor Red
            Write-Host "Available actions: setup, commit, simple, daemon, install, status" -ForegroundColor Yellow
        }
    }
}
