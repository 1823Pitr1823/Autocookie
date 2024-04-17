# Autocookie
  Automatic clicker will click your cookies for you. While you can brag to your friends,
  how much cookies you have and yet you still have a life.

## Platforms
  Windows
  
  Linux
  
## Requirements
  [Python](https://www.python.org/)

## Install
### Windows
  1. Install [Python](https://www.python.org/), in setup make sure to install pip as well.
  2. Start venv_install.bat script
  3. Run launch.bat
### Linux
  1. Install python using your package manager if not installed by default
  2. Start venv_install.sh
  3. Run launch.sh
  
## Usage
  Run launch file ".bat" for Windows ".sh" for linux.
  Activation key is "C", key can be locked using system tray digalog "Lock" to prevent accidental activation.
  
## Linux Compatibility Note:
  If you are running app on Wayland the keypress detection might not work for you unless key pressed over XWayland windows.
  This is primarily caused by way the wayland treats key capture. Running under root or with elevated privileges might resolve the issue,
  but most of the times result in error "failed to detected monitor".
  For these reasons it is recommended to run apps under XWayland.
  
  Example for browser using GTK: `GDK_BACKEND=x11 your_browser`
  
