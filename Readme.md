# Windows Automation Toolkit v2.0

A comprehensive, modular Windows 10/11 optimization and productivity toolkit that automates system tweaks, software installation, and configuration tasks.

## 🏗️ Architecture

This toolkit has been completely redesigned with a modular, scalable architecture:

```
windows-automation-toolkit/
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py          # Configuration settings
│   ├── utils/
│   │   ├── __init__.py
│   │   └── system.py            # Core system utilities
│   └── modules/
│       ├── __init__.py
│       ├── debloat.py           # Windows debloat & tweaks
│       ├── settings.py          # Windows settings & run commands
│       ├── power.py             # Power management
│       ├── installer.py         # App installation
│       ├── ai_tools.py          # AI tools installation
│       └── autohotkey.py        # AutoHotKey management
├── main.py                      # Main entry point
├── setup.py                     # Package setup
├── requirements.txt             # Dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

## 🚀 Features

### 🔧 Core Functionality
- **Administrator Detection**: Automatically detects and requests admin privileges
- **Modular Architecture**: Each feature is a separate, extensible module
- **Safety Confirmations**: User confirmation before all system operations
- **Error Handling**: Comprehensive error handling with clear status messages

### 🛠️ Available Modules

1. **Windows Debloat & Tweaks** (`debloat.py`)
   - Win11Debloat (raphi.re)
   - Debloat11 (git.io)
   - Windows Tweaks (christitus.com)
   - Windows Activation (get.activated.win)

2. **Windows Settings & Run Commands** (`settings.py`)
   - Performance Options
   - System Properties
   - Power Options
   - Programs and Features
   - Network Connections

3. **Power Management** (`power.py`)
   - Ultimate Performance plan unlocker
   - Power plan switching
   - Custom power plan creation
   - Power plan import/export

4. **App Installer** (`installer.py`)
   - Winget-based app installation
   - Batch installation support
   - App status checking
   - Custom app management

5. **AI Tools Installer** (`ai_tools.py`)
   - OpenCode AI
   - Qwen Code CLI
   - iFlow CLI
   - npm package management

6. **AutoHotKey Manager** (`autohotkey.py`)
   - AutoHotKey installation
   - Script creation and management
   - Startup integration
   - Script status monitoring

## 📋 Requirements

- Windows 10/11
- Python 3.10+
- Administrator privileges (recommended)
- Internet connection (for downloads)
- Windows Package Manager (winget) - for app installation

## 🛠️ Installation

1. Clone or download this repository
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the toolkit:
   ```bash
   python main.py
   ```

## 🚀 Usage

The toolkit features a clean menu-driven interface:

1. **Launch**: Run `python main.py`
2. **Admin Check**: Toolkit will detect admin privileges and offer to relaunch
3. **Main Menu**: Choose from 6 main modules
4. **Module Menus**: Each module has its own submenu with specific options
5. **Confirmation**: All operations require user confirmation
6. **Feedback**: Clear success/failure messages with emoji indicators

## 🔧 Extending the Toolkit

The modular architecture makes it easy to add new functionality:

### Adding a New Module

1. Create a new file in `src/modules/`
2. Inherit from base patterns in existing modules
3. Import and initialize in `main.py`
4. Add menu option to `UI_CONFIG` in `settings.py`

### Adding Configuration

1. Add settings to `src/config/settings.py`
2. Import in your module
3. Use configuration instead of hardcoded values

### Adding System Utilities

1. Add utility functions to `src/utils/system.py`
2. Make them available to all modules

## 🎯 AutoHotKey Script

The included AutoHotKey script provides:
- **F3 → Left Mouse Button**: Full mouse control using F3 key
- **Middle Mouse → Back**: Browser back navigation with middle mouse button

Script location: `Documents\AutoHotKey\automation.ahk`

## ⚡ Performance

- **Modular Loading**: Only load modules when needed
- **Efficient Commands**: Optimized PowerShell and subprocess calls
- **Timeout Handling**: Prevent hanging operations
- **Memory Management**: Clean resource handling

## 🛡️ Safety Features

- **User Confirmation**: All system operations require explicit consent
- **Command Transparency**: Shows commands before execution
- **Error Handling**: Graceful error handling with clear messages
- **Non-Destructive**: No permanent changes without user consent
- **Rollback Support**: Easy to undo changes where possible

## 🧪 Testing

The modular structure makes testing easier:

```bash
# Test individual modules
python -c "from src.modules.debloat import WindowsDebloat; print('✅ Debloat module works')"

# Test configuration
python -c "from src.config.settings import UI_CONFIG; print('✅ Config works')"

# Test utilities
python -c "from src.utils.system import SystemUtils; print('✅ Utils work')"
```

## 🔄 Updates

The modular architecture allows for easy updates:

- **Module Updates**: Update individual modules without affecting others
- **Configuration Updates**: Centralized configuration management
- **Dependency Management**: Clear dependency structure

## 📝 License

This toolkit is provided for educational and personal use. Use at your own risk.

## 🤝 Contributing

The modular structure makes contributions easy:

1. Fork the repository
2. Create a new branch for your feature
3. Add or modify modules in `src/modules/`
4. Update configuration if needed
5. Test your changes
6. Submit a pull request

## 🐛 Troubleshooting

- **Winget not found**: Install Windows Package Manager from Microsoft Store
- **PowerShell scripts blocked**: Run as administrator for proper execution
- **Node.js required**: Install Node.js via Essential Apps installer before AI tools
- **Module import errors**: Check Python path and ensure all `__init__.py` files exist

## 📊 Version History

- **v2.0.0**: Complete modular rewrite with scalable architecture
- **v1.0.0**: Original monolithic implementation