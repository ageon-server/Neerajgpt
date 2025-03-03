import openai
import config

openai.api_key = config.AI_API_KEY

def init(app):
    @app.on_message(filters.text & filters.private)
    def ai_reply(_, message):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.text}]
        )
        message.reply_text(response['choices'][0]['message']['content'])
