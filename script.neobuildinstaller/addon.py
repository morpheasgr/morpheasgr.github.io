import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Set a string variable to use 
line1 = "This is a faux addon, just to abuse imports. Completely useless unless called by a build."

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
xbmcgui.Dialog().ok(addonname, line1)
