# Power.sh

Automated Windows post-installation setup with essential apps, CLI tools, and system optimization.

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
- **Startup Optimization**: Review and management of startup programs

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



## Legend

- **[AUTO]** Runs without user input
- **[USER]** Requires explicit user approval
- **[MANUAL]** User must manually verify/configure
- **[OPTIONAL]** User can choose to skip
- **[ADMIN]** Requires Administrator privileges
- **[FALLBACK]** Has alternative if primary method fails
- **[MIXED]** Combination of automatic and manual steps

## Safety Features

1. **Comprehensive Logging**: All actions logged to `logs/setup-session-[timestamp].log`
2. **Modular Execution**: Each phase can be skipped or re-run independently
3. **Error Handling**: Graceful failure handling with clear error messages
4. **Security Warnings**: Explicit warnings for remote script execution
5. **Registry Backups**: Automatic backups before making registry changes

## File Structure

```
C:\Project Files\Power Es Aech\
├── bin/
│   └── run.sh                    # Main bash orchestration script
├── scripts/
│   ├── common-functions.ps1      # Shared PowerShell utilities & logging
│   ├── debloat-selection.ps1     # Interactive debloat script selection
│   ├── power-plan.ps1           # Ultimate Performance power plan setup
│   ├── install-apps.ps1         # Essential applications installation
│   ├── cli-tools.ps1            # Terminal AI CLI tools setup
│   ├── autohotkey-setup.ps1     # AutoHotkey configuration & deployment
│   ├── system-settings.ps1      # System settings automation
│   └── mouse-remap.ahk          # AutoHotkey script template
├── logs/                        # Auto-created for session logs & backups
├── execution-plan.md            # Detailed execution plan documentation
└── README.md                    # This file
```

## Expected Runtime

- **Full execution**: 15-30 minutes
- **Minimal setup** (skip debloat): 5-10 minutes
- **User interaction time**: 2-5 minutes total

**Note:** Runtime may vary based on:
- Internet connection speed
- System performance
- Package availability
- User response time for confirmations

## Troubleshooting

### Common Issues

1. **"PowerShell not found"**
   - Ensure you're running on Windows with PowerShell installed
   - Try running from Git Bash or WSL

2. **"Administrator privileges required"**
   - Run PowerShell as Administrator
   - Use the provided elevation command in the script output

3. **"Package manager not available"**
   - The script will attempt to install winget and/or chocolatey automatically
   - Ensure internet connection is available

4. **"AutoHotkey script not working"**
   - Verify AutoHotkey v2 is installed (not v1)
   - Check if antivirus is blocking the script
   - Manually run the script from `Documents\AutoHotkey\mouse-remap.ahk`

### Log Files

Check the session log for detailed information:
```
logs/setup-session-[timestamp].log
```

## Manual Verification Steps

After running the script, manually verify:

1. **Power Plan**: Settings > System > Power & battery → "Ultimate Performance" selected
2. **Applications**: All installed applications launch correctly
3. **AutoHotkey**: F3 acts as left mouse button, middle mouse goes back
4. **CLI Tools**: Open new terminal and test:
   ```bash
   opencode --version
   qwen-code --version
   iflow --version
   ```



## Customization

To modify the script behavior:

1. **Add/Remove Applications**: Edit the `$Applications` array in `scripts/install-apps.ps1`
2. **Add/Remove CLI Tools**: Edit the `$CLITools` array in `scripts/cli-tools.ps1`
3. **Modify AutoHotkey Script**: Edit the script content in `scripts/autohotkey-setup.ps1`
4. **Change System Settings**: Modify registry operations in `scripts/system-settings.ps1`
5. **Adjust Debloat Options**: Edit available scripts in `scripts/debloat-selection.ps1`

### Advanced Customization
- **Logging Configuration**: Modify logging levels and output locations in `scripts/common-functions.ps1`
- **Error Handling**: Adjust retry logic and timeout values in individual modules
- **Registry Settings**: Add custom registry modifications to the system settings module
- **Network Configuration**: Modify download sources and fallback URLs

## Security Considerations

- **Remote Scripts**: The debloat options download and execute scripts from remote sources
- **Registry Changes**: The script modifies Windows registry for performance optimizations
- **Administrator Access**: Many features require elevated privileges
- **Antivirus**: Some antivirus software may flag AutoHotkey scripts

Always review the code before running and ensure you trust the remote script sources if you choose to use them.

## Requirements & Dependencies

### System Requirements
- **Operating System**: Windows 10 or Windows 11
- **Processor**: x64 or ARM64 architecture
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB free space for applications and logs

### Software Dependencies
- **PowerShell 5.1+** (included with Windows)
- **Git Bash, WSL, or equivalent bash environment**
- **Internet connection** for downloading applications and tools

### Optional Dependencies
- **Administrator privileges** for full functionality
- **Windows Package Manager (winget)** - auto-installed if missing
- **Chocolatey** - fallback package manager, auto-installed if needed

