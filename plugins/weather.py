import requests
from pyrogram import filters

def init(app):
    @app.on_message(filters.command("weather"))
    def weather(_, message):
        city = message.text.split(" ", 1)[1]
        response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}")
        data = response.json()
        message.reply_text(f"Weather in {city}: {data['current']['temp_c']}°C, {data['current']['condition']['text']}")
