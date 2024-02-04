Automatic clicker will click your cookies for you. While you can brag to your friends how much cookies you have and yet you still have a life.

Compatibility Note:
  If you are running app on Wayland the keypress detection might not work for you unless key pressed over XWayland windows.
  This is primarily caused by way wayland treats listening to keystrokes due to security reasons. Running under root or with elevated privileges might resolve the issues,
  but most of the times result in error failed to detected monitor.
  For these reasons it is recommended to have installed Xorg when using for browser and running browser with GDK_BACKEND=x11.
  Example:
    GDK_BACKEND=x11 your_browser
