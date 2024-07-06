Rem I created this script because when I let the installer handle the creation of the shortcut is doesn't appear in the context menu inside "send to".
Rem I couln't find an answer, if you know please let me know why this happens.
Set objShell = CreateObject("WScript.Shell")

Rem Retrieve the installation directory (TARGETDIR)
Rem installDir = objShell.ExpandEnvironmentStrings("[TARGETDIR]")
installDir = Session.Property("CustomActionData")


Rem Construct the full path to your executable
exePath = installDir & "Wazzapp.exe"

Rem Path to the SendTo folder
sendToPath = objShell.SpecialFolders("SendTo")

Rem Create a shortcut in the SendTo folder
shortcutName = "Wazzapp (fix WhatsApp jpeg images for Photoshop).lnk"
shortcutPath = sendToPath & "\" & shortcutName

Set objShortcut = objShell.CreateShortcut(shortcutPath)
objShortcut.TargetPath = exePath
objShortcut.Save