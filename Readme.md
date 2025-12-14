# Power.sh

Automated Windows post-installation setup with essential apps, CLI tools, and system optimization.

## Quick Start

1. **Prerequisites**:
   - Windows 10 or Windows 11
   - Git Bash, WSL, or similar bash environment
   - Internet connection

2. **Run the script**:
   ```bash
   # For full functionality (recommended)
   # Run PowerShell as Administrator, then:
   cd "C:\Project Files\Power Es Aech"
   bash bin/run.sh
   
   # Or from PowerShell:
   Start-Process powershell -Verb RunAs -ArgumentList '-Command "cd \"C:\Project Files\Power Es Aech\"; bash bin/run.sh"'
   ```

## Features

### Automation Capabilities
- **One-Command Setup**: Complete Windows post-installation automation
- **Smart Package Management**: Winget primary, Chocolatey fallback
- **PowerShell Automation**: System-level configuration and optimization
- **Cross-Shell Support**: Compatible with PowerShell, Git Bash, and WSL

### Safety & Control
- **Modular Design**: 7 independent steps - run what you need
- **Comprehensive Logging**: Detailed session logs with timestamps
- **User Confirmation**: Explicit approval for risky operations
- **Registry Backups**: Automatic backups before system changes
- **Graceful Degradation**: Continues even when some steps fail

### Developer Tools
- **IDE Installation**: VS Code with default settings
- **Version Control**: Git configuration and setup
- **Runtime Environment**: Node.js LTS with npm
- **CLI Tools**: OpenCode AI, Qwen Code CLI, iFlow CLI
- **Automation Scripts**: AutoHotkey v2 with mouse remapping

### System Optimization
- **Performance Tuning**: Ultimate Performance power plan activation
- **Privacy Hardening**: Telemetry and advertising ID management
- **Debloating**: Optional removal of Windows bloatware
- **Visual Effects**: Performance-oriented display settings
- **Startup Optimization**: Review and management of stash rtup programs


