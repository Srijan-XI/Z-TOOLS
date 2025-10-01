# Winget CLI Tool

A Python-based CLI tool to manage Windows applications via Winget.

## Features
- List Upgradable Packages
- Upgrade All Packages
- Install/Uninstall Applications
- Source Management
- Action Logging (log.txt)

## Usage
``` 
python main.py 
``` 
## File Structure

```
winget_cli_tool/
│
├── main.py                # CLI menu and main entry point
├── winget_manager.py      # All Winget-related commands + logging
├── log.txt                # Auto-created; logs Install/Uninstall actions
├── README.md              # Documentation
└── requirements.txt       # (Optional — no external libraries needed)

```