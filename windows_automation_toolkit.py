#!/usr/bin/env python3
"""
Windows Automation Toolkit
A comprehensive Windows 10/11 optimization and productivity toolkit
Author: AI Assistant
Version: 1.0
"""

import os
import sys
import ctypes
import subprocess
import time
import requests
from pathlib import Path
import json


class WindowsAutomationToolkit:
    def __init__(self):
        self.is_admin = self.check_admin_privileges()
        self.user_profile = os.path.expanduser("~")
        self.documents_folder = os.path.join(self.user_profile, "Documents")
        
    def check_admin_privileges(self):
        """Check if the script is running with administrator privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def relaunch_as_admin(self):
        """Relaunch the script with administrator privileges"""
        if not self.is_admin:
            try:
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1
                )
                sys.exit(0)
            except Exception as e:
                print(f"❌ Failed to relaunch as admin: {e}")
                return False
        return True
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pause_execution(self):
        """Pause execution and wait for user input"""
        input("\n⏸️ Press Enter to continue...")
    
    def print_header(self):
        """Print the toolkit header"""
        self.clear_screen()
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                🛠️ WINDOWS AUTOMATION TOOLKIT 🛠️               ║")
        print("║                 Windows 10/11 Optimization Suite               ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print(f"👤 Running as: {'Administrator ✅' if self.is_admin else 'User ⚠️'}")
        print()
    
    def run_powershell_command(self, command, bypass_policy=True):
        """Execute a PowerShell command with optional execution policy bypass"""
        try:
            ps_command = command
            if bypass_policy:
                ps_command = f"-ExecutionPolicy Bypass -Command \"{command}\""
            
            print(f"🔧 Executing: {command}")
            result = subprocess.run(
                ["powershell", ps_command],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print("✅ Command executed successfully")
                if result.stdout.strip():
                    print(f"📄 Output: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ Command failed: {result.stderr.strip()}")
                return False
                
        except subprocess.TimeoutExpired:
            print("❌ Command timed out")
            return False
        except Exception as e:
            print(f"❌ Error executing command: {e}")
            return False
    
    def run_powershell_script(self, script_url, description):
        """Execute a PowerShell script from URL"""
        print(f"\n🚀 {description}")
        print("=" * 50)
        
        if not self.get_confirmation(f"Run {description}? This will execute PowerShell scripts from the internet."):
            print("❌ Operation cancelled by user")
            return False
        
        command = f"[scriptblock]::Create((irm \"{script_url}\"))"
        return self.run_powershell_command(command)
    
    def get_confirmation(self, message):
        """Get user confirmation for potentially risky operations"""
        while True:
            response = input(f"\n⚠️ {message} (y/n): ").lower().strip()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no")
    
    def windows_debloat_launcher(self):
        """Windows Debloat & Tweaks Launcher"""
        print("\n🧹 Windows Debloat & Tweaks")
        print("=" * 40)
        print("[1] Win11Debloat (raphi.re)")
        print("[2] Debloat11 (git.io)")
        print("[3] Windows Tweaks (christitus.com)")
        print("[4] Activate Windows (get.activated.win)")
        print("[0] Back to Main Menu")
        
        choice = input("\nSelect option: ").strip()
        
        scripts = {
            "1": ("https://win11debloat.raphi.re/", "Win11Debloat"),
            "2": ("https://git.io/debloat11", "Debloat11"),
            "3": ("https://christitus.com/win", "Windows Tweaks"),
            "4": ("https://get.activated.win", "Windows Activation")
        }
        
        if choice in scripts:
            url, desc = scripts[choice]
            success = self.run_powershell_script(url, desc)
            if success:
                print(f"✅ {desc} completed successfully")
            else:
                print(f"❌ {desc} failed")
            self.pause_execution()
        elif choice == "0":
            return
        else:
            print("❌ Invalid option")
            self.pause_execution()
    
    def windows_settings_launcher(self):
        """Windows Settings & Run Commands Automation"""
        print("\n⚙️ Windows Settings & Run Commands")
        print("=" * 40)
        print("[1] Performance Options")
        print("[2] System Properties")
        print("[3] Power Options")
        print("[4] Programs and Features")
        print("[5] Network Connections")
        print("[0] Back to Main Menu")
        
        commands = {
            "1": "SystemPropertiesPerformance",
            "2": "sysdm.cpl",
            "3": "powercfg.cpl",
            "4": "appwiz.cpl",
            "5": "ncpa.cpl"
        }
        
        choice = input("\nSelect option: ").strip()
        
        if choice in commands:
            command = commands[choice]
            try:
                print(f"🔧 Opening: {command}")
                subprocess.Popen(["cmd", "/c", "start", command], shell=True)
                print("✅ Command executed successfully")
                self.pause_execution()
            except Exception as e:
                print(f"❌ Failed to open {command}: {e}")
                self.pause_execution()
        elif choice == "0":
            return
        else:
            print("❌ Invalid option")
            self.pause_execution()
    
    def ultimate_performance_unlocker(self):
        """Ultimate Performance Power Plan Unlocker"""
        print("\n⚡ Ultimate Performance Power Plan Unlocker")
        print("=" * 50)
        
        if not self.get_confirmation("Unlock Ultimate Performance power plan?"):
            print("❌ Operation cancelled")
            return
        
        # Step 1: Duplicate the scheme
        print("\n🔧 Step 1: Duplicating Ultimate Performance scheme...")
        guid_command = "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"
        
        result = subprocess.run(
            ["powercfg", "-duplicatescheme", "e9a42b02-d5df-448d-aa00-03f14749eb61"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            # Extract GUID from output
            output = result.stdout.strip()
            guid = output.split()[-1] if output else None
            
            if guid:
                print(f"✅ Power plan created with GUID: {guid}")
                
                # Step 2: Ask if user wants to activate it
                if self.get_confirmation(f"Activate the Ultimate Performance plan now?"):
                    activate_command = f"powercfg -setactive {guid}"
                    if self.run_powershell_command(activate_command, bypass_policy=False):
                        print("✅ Ultimate Performance plan activated!")
                
                # Step 3: Show active scheme
                print("\n🔍 Current active power scheme:")
                subprocess.run(["powercfg", "/getactivescheme"])
                
                # Step 4: Open Power Options
                if self.get_confirmation("Open Power Options for visual confirmation?"):
                    subprocess.Popen(["powercfg.cpl"])
                    
            else:
                print("❌ Could not extract GUID from output")
        else:
            print(f"❌ Failed to duplicate power scheme: {result.stderr}")
        
        self.pause_execution()
    
    def check_winget_available(self):
        """Check if winget is available on the system"""
        try:
            result = subprocess.run(["winget", "--version"], capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False
    
    def install_app_winget(self, app_id, app_name):
        """Install application using winget"""
        print(f"📦 Installing {app_name}...")
        
        try:
            result = subprocess.run(
                ["winget", "install", "--id", app_id, "--accept-package-agreements", "--accept-source-agreements"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print(f"✅ {app_name} installed successfully")
                return True
            else:
                print(f"❌ Failed to install {app_name}: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"❌ Installation of {app_name} timed out")
            return False
        except Exception as e:
            print(f"❌ Error installing {app_name}: {e}")
            return False
    
    def essential_apps_downloader(self):
        """Essential Apps Downloader"""
        print("\n📦 Essential Apps Downloader")
        print("=" * 40)
        
        if not self.check_winget_available():
            print("❌ Winget is not available. Please install Windows Package Manager first.")
            self.pause_execution()
            return
        
        apps = [
            ("Microsoft.VisualStudioCode", "Visual Studio Code"),
            ("Yandex.Browser", "Yandex Browser"),
            ("OpenJS.NodeJS", "Node.js LTS"),
            ("Git.Git", "Git"),
            ("AutoHotkey.AutoHotkey", "AutoHotKey")
        ]
        
        print("Available apps to install:")
        for i, (app_id, app_name) in enumerate(apps, 1):
            print(f"[{i}] {app_name}")
        
        print("[0] Back to Main Menu")
        print("[99] Install All Apps")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "0":
            return
        elif choice == "99":
            if not self.get_confirmation("Install all essential apps? This may take several minutes."):
                print("❌ Operation cancelled")
                return
            
            for app_id, app_name in apps:
                self.install_app_winget(app_id, app_name)
                time.sleep(2)
        elif choice.isdigit() and 1 <= int(choice) <= len(apps):
            app_id, app_name = apps[int(choice) - 1]
            self.install_app_winget(app_id, app_name)
        else:
            print("❌ Invalid option")
        
        self.pause_execution()
    
    def check_node_npm_available(self):
        """Check if Node.js and npm are available"""
        try:
            node_result = subprocess.run(["node", "--version"], capture_output=True, text=True)
            npm_result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
            return node_result.returncode == 0 and npm_result.returncode == 0
        except FileNotFoundError:
            return False
    
    def install_terminal_ai_tools(self):
        """Terminal AI Tools Installer"""
        print("\n🤖 Terminal AI Tools Installer")
        print("=" * 40)
        
        if not self.check_node_npm_available():
            print("❌ Node.js and npm are not available.")
            print("Please install Node.js first using the Essential Apps Downloader.")
            self.pause_execution()
            return
        
        tools = [
            ("opencode-ai", "OpenCode AI"),
            ("@qwen-code/qwen-code@latest", "Qwen Code CLI")
        ]
        
        print("Available AI tools to install:")
        for i, (package, name) in enumerate(tools, 1):
            print(f"[{i}] {name}")
        
        print("[3] iFlow CLI")
        print("[0] Back to Main Menu")
        print("[99] Install All Tools")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "0":
            return
        elif choice == "99":
            if not self.get_confirmation("Install all AI tools?"):
                print("❌ Operation cancelled")
                return
            
            for package, name in tools:
                print(f"\n📦 Installing {name}...")
                result = subprocess.run(["npm", "install", "-g", package], capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"✅ {name} installed successfully")
                else:
                    print(f"❌ Failed to install {name}: {result.stderr}")
                time.sleep(2)
            
            # Install iFlow CLI
            self.install_iflow_cli()
            
        elif choice.isdigit() and 1 <= int(choice) <= len(tools):
            package, name = tools[int(choice) - 1]
            print(f"\n📦 Installing {name}...")
            result = subprocess.run(["npm", "install", "-g", package], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ {name} installed successfully")
            else:
                print(f"❌ Failed to install {name}: {result.stderr}")
        elif choice == "3":
            self.install_iflow_cli()
        else:
            print("❌ Invalid option")
        
        self.pause_execution()
    
    def install_iflow_cli(self):
        """Install iFlow CLI"""
        print("\n📦 Installing iFlow CLI...")
        if self.get_confirmation("Install iFlow CLI? This will run a bash command."):
            try:
                # Note: iFlow CLI installation uses bash, which may not be available on Windows
                # This would require WSL or Git Bash to work properly
                print("⚠️ iFlow CLI requires bash environment (WSL or Git Bash)")
                print("Please run this command manually in bash:")
                print('curl -fsSL https://cloud.iflow.cn/iflow-cli/install.sh | bash')
            except Exception as e:
                print(f"❌ Error installing iFlow CLI: {e}")
    
    def setup_autohotkey(self):
        """AutoHotKey Setup & Script Deployment"""
        print("\n🎹 AutoHotKey Setup & Script Deployment")
        print("=" * 40)
        
        # Check if AutoHotKey is installed
        try:
            result = subprocess.run(["AutoHotkey64.exe", "--version"], capture_output=True, text=True)
            ahk_installed = result.returncode == 0
        except FileNotFoundError:
            ahk_installed = False
        
        if not ahk_installed:
            print("❌ AutoHotKey is not installed.")
            if self.get_confirmation("Install AutoHotKey first?"):
                if not self.check_winget_available():
                    print("❌ Winget is not available. Please install AutoHotKey manually.")
                    self.pause_execution()
                    return
                
                if self.install_app_winget("AutoHotkey.AutoHotkey", "AutoHotKey"):
                    print("✅ AutoHotKey installed successfully")
                else:
                    print("❌ Failed to install AutoHotKey")
                    self.pause_execution()
                    return
            else:
                print("❌ AutoHotKey installation skipped")
                self.pause_execution()
                return
        
        # Create AutoHotKey directory
        ahk_dir = os.path.join(self.documents_folder, "AutoHotKey")
        os.makedirs(ahk_dir, exist_ok=True)
        
        # Create the automation script
        script_content = """; ===============================
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
        
        script_path = os.path.join(ahk_dir, "automation.ahk")
        
        try:
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(script_content)
            print(f"✅ AutoHotKey script created at: {script_path}")
            
            # Ask if user wants to add to startup
            if self.get_confirmation("Add AutoHotKey script to Windows startup?"):
                startup_folder = os.path.join(
                    os.environ['APPDATA'], 
                    'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup'
                )
                shortcut_path = os.path.join(startup_folder, "automation.ahk")
                
                # Create a copy in startup folder
                import shutil
                shutil.copy2(script_path, shortcut_path)
                print(f"✅ Script added to startup: {shortcut_path}")
            
            # Ask if user wants to run the script now
            if self.get_confirmation("Run the AutoHotKey script now?"):
                subprocess.Popen(["AutoHotkey64.exe", script_path])
                print("✅ AutoHotKey script is now running")
                
        except Exception as e:
            print(f"❌ Error creating AutoHotKey script: {e}")
        
        self.pause_execution()
    
    def main_menu(self):
        """Display the main menu and handle user input"""
        while True:
            self.print_header()
            
            print("🚀 MAIN MENU")
            print("=" * 40)
            print("[1] 🧹 Windows Debloat & Tweaks")
            print("[2] ⚙️ Windows Settings & Run Commands")
            print("[3] ⚡ Unlock Ultimate Performance")
            print("[4] 📦 Install Essential Apps")
            print("[5] 🤖 Install Terminal AI Tools")
            print("[6] 🎹 Setup AutoHotKey")
            print("[0] 🚪 Exit")
            print()
            
            choice = input("Select option: ").strip()
            
            if choice == "1":
                self.windows_debloat_launcher()
            elif choice == "2":
                self.windows_settings_launcher()
            elif choice == "3":
                self.ultimate_performance_unlocker()
            elif choice == "4":
                self.essential_apps_downloader()
            elif choice == "5":
                self.install_terminal_ai_tools()
            elif choice == "6":
                self.setup_autohotkey()
            elif choice == "0":
                print("\n👋 Thank you for using Windows Automation Toolkit!")
                print("🔧 Your Windows system has been optimized! 🚀")
                break
            else:
                print("❌ Invalid option. Please try again.")
                self.pause_execution()
    
    def run(self):
        """Main entry point for the toolkit"""
        # Check admin privileges and relaunch if needed
        if not self.is_admin:
            print("⚠️ This toolkit requires administrator privileges for full functionality.")
            if self.get_confirmation("Relaunch as Administrator?"):
                if self.relaunch_as_admin():
                    return
            else:
                print("⚠️ Some features may not work without administrator privileges.")
                self.pause_execution()
        
        # Start the main menu
        self.main_menu()


def main():
    """Main function"""
    try:
        toolkit = WindowsAutomationToolkit()
        toolkit.run()
    except KeyboardInterrupt:
        print("\n\n👋 Operation cancelled by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        input("Press Enter to exit...")


if __name__ == "__main__":
    main()