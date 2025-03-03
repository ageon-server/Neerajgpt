import requests
from pyrogram import filters

def init(app):
    @app.on_message(filters.command("insta"))
    def insta_download(_, message):
        url = message.text.split(" ", 1)[1]
        response = requests.get(f"https://some-insta-api.com/download?url={url}")
        if response.status_code == 200:
            message.reply_video(response.json()["url"])
        else:
            message.reply_text("Download Failed!")
