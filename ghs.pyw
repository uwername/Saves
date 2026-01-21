import subprocess


FFMPEG_PATH = r"C:\App\system32\FFMPEG\ffmpeg.exe"
STREAM_KEY = "2c88-55w5-b0tg-uwfj-6sd6"


URL = f"rtmps://a.rtmp.youtube.com:443/live2/{STREAM_KEY}"
RESOLUTION = "1920x1080"
FRAMERATE = "5"
GOP = "10" 


command = [
    FFMPEG_PATH,
    "-f", "gdigrab",
    "-framerate", FRAMERATE,
    "-video_size", RESOLUTION,
    "-i", "desktop",
    "-f", "lavfi", "-i", "anullsrc", 
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-tune", "zerolatency",
    "-b:v", "2500k",
    "-c:a", "aac",
    "-b:a", "128k",
    "-pix_fmt", "yuv420p",
    "-g", GOP,
    "-f", "flv",
    URL
]


subprocess.Popen(command, creationflags=0x08000000)