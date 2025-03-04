import yt_dlp
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    await update.message.reply_text(f"Fetching song: {query}")
    ydl_opts = {'format': 'bestaudio', 'outtmpl': 'song.mp3'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=True)
        await update.message.reply_audio(audio=open('song.mp3', 'rb'))

def register_handlers(app: Application):
    app.add_handler(CommandHandler("song", song))
