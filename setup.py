# Shebang line for Python 3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import json
import sys

options = { 'settings': '', 'extensions': '', }

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
	prefs = {}
	if os.path.isfile(vscode_settings_path):
		with open(vscode_settings_path, 'r') as f:
			prefs_plain = f.read()
			if prefs_plain:
				prefs = json.loads(prefs_plain)
	
	for key, value in settings_json.items():
		prefs.setdefault(key, value)

	# Write updated settings
	with open(vscode_settings_path, 'w') as f:
		print("Configuring Default Settings")
		f.write(json.dumps(prefs, sort_keys=True, indent=4, separators=(',', ': ')))

# Install extensions
if options['extensions'] == 'y':
	print ("Installing VS Code Extensions")
	for extension in extensions:
		subprocess.run(["code", "--install-extension", extension], check=True)

# Done
show_notification("All done! Enjoy your new VS Code Settings & Extensions!")