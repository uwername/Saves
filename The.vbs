Set WshShell = CreateObject("WScript.Shell")
' The "0" at the end is the magic number that hides the window
WshShell.Run chr(34) & "C:\Apps\system32\FFMPEG\stream.bat" & chr(34), 0
Set WshShell = Nothing