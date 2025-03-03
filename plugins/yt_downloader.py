from yt_dlp import YoutubeDL
from pyrogram import filters

def init(app):
    @app.on_message(filters.command("yt"))
    def yt_download(_, message):
        url = message.text.split(" ", 1)[1]
        with YoutubeDL({"format": "best"}) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info["url"]
            message.reply_video(video_url)
