Set objShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

Rem Path to the SendTo folder
sendToPath = objShell.SpecialFolders("SendTo")

Rem Specify the name of the shortcut to remove (adjust as per your actual shortcut name)
shortcutName = "Wazzapp (fix WhatsApp jpeg images for Photoshop).lnk"

Rem Construct the full path to the shortcut
shortcutPath = sendToPath & "\" & shortcutName

Rem Check if the shortcut exists before attempting to delete it
If fso.FileExists(shortcutPath) Then
    fso.DeleteFile(shortcutPath)
End If
