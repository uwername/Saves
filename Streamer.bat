











@echo off
set FFMPEG_PATH=C:\App\system32\FFMPEG\ffmpeg.exe

:: --- PASTE YOUR KEY BELOW ---
set KEY=2c88-55w5-b0tg-uwfj-6sd6

:: --- SETTINGS ---
set URL=rtmps://a.rtmp.youtube.com:443/live2/%KEY%

:: Resolution (1080p)
set RES=1920x1080

echo [INFO] Starting Stream at 5 FPS...

:: The Command
:: Changed -framerate to 5
:: Changed -g to 10 (Critical for stability at low FPS)
"%FFMPEG_PATH%" -f gdigrab -framerate 5 -video_size %RES% -i desktop -f lavfi -i anullsrc -c:v libx264 -preset ultrafast -tune zerolatency -b:v 2500k -c:a aac -b:a 128k -pix_fmt yuv420p -g 10 -f flv "%URL%"

pause