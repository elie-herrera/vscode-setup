# Shebang line for Python 3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import json
import sys

options = { 'settings': '', 'extensions': '', }

def read_json_file(file_path):
	try:
		with open(file_path, 'r') as file:
			return json.load(file)
	except json.JSONDecodeError:
		print(f"Error: {file_path} contains invalid JSON. Please check the file format.")
		sys.exit(1)
	except FileNotFoundError:
		print(f"Error: {file_path} not found. A new file will be created.")
	except Exception as e:
		print(f"Unexpected error reading {file_path}: {e}")
		sys.exit(1)
	return {}

def write_json_file(file_path, data):
	try:
		with open(file_path, 'w') as file:
			json.dump(data, file, sort_keys=True, indent=4, separators=(',', ': '))
	except Exception as e:
		print(f"Unexpected error writing to {file_path}: {e}")

# Welcome Message
print ("\n\nHi ... Welcome to VS Code Setup\n")

# Setup Options
while options['settings'] not in ['y', 'n']:
	options['settings'] = input("Do you want to install default VSCode User Settings? (%s)  " % '|'.join(['y','n']))

while options['extensions'] not in ['y', 'n']:
	options['extensions'] = input("Do you want to install some cool Extensions? (%s)  " % '|'.join(['y','n']))

def show_notification(text):
  os.system('osascript -e \'display notification "'+ text +'" with title "VS Code Setup"\' > /dev/null')

# Path to VSCode settings for macOS
vscode_settings_path = os.path.expanduser('~/Library/Application Support/Code/User/settings.json')

# Desired settings - Customize this as per your requirement
settings_json = {
  "editor.minimap.enabled": False,
	"workbench.startupEditor": "none",
	"cSpell.enabled": False,
	"files.autoSave": "onFocusChange",
	"editor.tabSize": 2,
	"window.nativeTabs": True,
	"editor.wordWrap": "on",
	"editor.renderWhitespace": "none",
	"editor.fontSize": 14,
	"window.zoomLevel": 1,
	"editor.glyphMargin": False,
}

# List of extensions to install - Customize this list
extensions = [
	"formulahendry.auto-rename-tag",
	"formulahendry.auto-close-tag",
  "chouzz.vscode-better-align",
  "streetsidesoftware.code-spell-checker",
  "dbaeumer.vscode-eslint",
  "eamodio.gitlens",
  "zignd.html-css-class-completion",
  "cardinal90.multi-cursor-case-preserve",
  "dawhite.mustache",
  "christian-kohler.path-intellisense",
  "esbenp.prettier-vscode",
	"ms-python.python",
]

# Customization for VSCode
if options['settings'] == 'y':
	print("Customizing VS Code User Settings")
	
	# Check if VSCode is installed by looking for the application
	if not os.path.exists('/Applications/Visual Studio Code.app'):
		print("VS Code is not installed. Please install it first.")
		sys.exit(1)

	# Ensure VSCode settings directory exists
	if not os.path.exists(os.path.dirname(vscode_settings_path)):
		os.makedirs(os.path.dirname(vscode_settings_path))

	# Read existing settings and update them
	prefs = read_json_file(vscode_settings_path)
	for key, value in settings_json.items():
		prefs.setdefault(key, value)

	# Write updated settings
	print("Configuring Default Settings")
	write_json_file(vscode_settings_path, prefs)

# Install extensions
if options['extensions'] == 'y':
	print ("Installing VS Code Extensions")
	for extension in extensions:
		try:
			subprocess.run(["code", "--install-extension", extension], check=True)
		except subprocess.CalledProcessError as e:
			print(f"Failed to install extension {extension}: {e}")
		except Exception as e:
			print(f"Unexpected error installing extension {extension}: {e}")

# Done
show_notification("All done! Enjoy your new VS Code!")