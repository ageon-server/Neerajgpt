import random
from pyrogram import filters

roasts = ["तेरी तो ऐसी की तैसी!", "कहाँ से आते हो लोग?", "तेरे jokes से अच्छे मेरे बूट के तले हैं!"]
love_msgs = ["तू मेरे दिल का राजा!", "तेरे बिना जिंदगी अधूरी है!", "I love you 3000!"]
truths = ["तेरी सबसे बड़ी गलती क्या थी?", "अब तक का सबसे बड़ा झूठ क्या बोला?"]
dares = ["Public में गाना गा!", "अपने crush को message कर!"]
facts = ["हाथी उड़ नहीं सकते!", "समुद्र का पानी खारा क्यों होता है?", "तुम्हारी हंसी सबसे प्यारी है!"]

def init(app):
    @app.on_message(filters.command("roast"))
    def roast(_, message):
        message.reply_text(random.choice(roasts))

    @app.on_message(filters.command("love"))
    def love(_, message):
        message.reply_text(random.choice(love_msgs))

    @app.on_message(filters.command("truth"))
    def truth(_, message):
        message.reply_text(random.choice(truths))

    @app.on_message(filters.command("dare"))
    def dare(_, message):
        message.reply_text(random.choice(dares))

    @app.on_message(filters.command("fact"))
    def fact(_, message):
        message.reply_text(random.choice(facts))
