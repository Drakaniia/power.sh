"""
Configuration settings for Windows Automation Toolkit
"""

# PowerShell Scripts Configuration
POWERSHELL_SCRIPTS = {
    "debloat": {
        "win11debloat": {
            "name": "Win11Debloat",
            "url": "https://win11debloat.raphi.re/",
            "description": "Comprehensive Windows 11 debloating"
        },
        "debloat11": {
            "name": "Debloat11",
            "url": "https://git.io/debloat11",
            "description": "Alternative Windows 11 debloating"
        }
    },
    "tweaks": {
        "windows_tweaks": {
            "name": "Windows Tweaks",
            "url": "https://christitus.com/win",
            "description": "Windows performance and UI tweaks"
        }
    },
    "activation": {
        "activate_windows": {
            "name": "Windows Activation",
            "url": "https://get.activated.win",
            "description": "Windows activation script"
        }
    }
}

# Windows Run Commands
WINDOWS_COMMANDS = {
    "performance": "SystemPropertiesPerformance",
    "system": "sysdm.cpl",
    "power": "powercfg.cpl",
    "programs": "appwiz.cpl",
    "network": "ncpa.cpl"
}

# Essential Apps Configuration
ESSENTIAL_APPS = [
    {"id": "Microsoft.VisualStudioCode", "name": "Visual Studio Code"},
    {"id": "Yandex.Browser", "name": "Yandex Browser"},
    {"id": "OpenJS.NodeJS", "name": "Node.js LTS"},
    {"id": "Git.Git", "name": "Git"},
    {"id": "AutoHotkey.AutoHotkey", "name": "AutoHotKey"}
]

# Terminal AI Tools Configuration
AI_TOOLS = [
    {"package": "opencode-ai", "name": "OpenCode AI"},
    {"package": "@qwen-code/qwen-code@latest", "name": "Qwen Code CLI"}
]

# Power Plan Configuration
ULTIMATE_PERFORMANCE_GUID = "e9a42b02-d5df-448d-aa00-03f14749eb61"

# AutoHotKey Script Content
AHK_SCRIPT_CONTENT = """; ===============================
; Full F3 -> Left Mouse Button
; ===============================

#Requires AutoHotkey v2.0

; --- Single Click / Hold / Drag ---
F3::
{
    SendInput("{LButton down}")   ; Press & hold left button
    KeyWait("F3")                 ; Wait until F3 is released
    SendInput("{LButton up}")     ; Release button
}

; AHK v2 version - Remap Middle Mouse Button to Back
MButton::Send("!{Left}")
"""

# UI Configuration
UI_CONFIG = {
    "header_title": "Windows Automation Toolkit",
    "header_subtitle": "Windows 10/11 Optimization Suite",
    "menu_options": {
        "1": {"title": "Windows Debloat & Tweaks", "icon": "🧹"},
        "2": {"title": "Windows Settings & Run Commands", "icon": "⚙️"},
        "3": {"title": "Unlock Ultimate Performance", "icon": "⚡"},
        "4": {"title": "Install Essential Apps", "icon": "📦"},
        "5": {"title": "Install Terminal AI Tools", "icon": "🤖"},
        "6": {"title": "Setup AutoHotKey", "icon": "🎹"},
        "0": {"title": "Exit", "icon": "🚪"}
    }
}

# System Paths
SYSTEM_PATHS = {
    "documents": "Documents",
    "startup": "APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Startup",
    "temp": "TEMP"
}