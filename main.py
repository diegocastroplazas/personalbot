from voice import Voice
import logging
from bot.bot import Bot
from bot.exceptions import DialogFailed

driver = Voice()
bot = Bot()

while 1:
    try:
        text = input("Type a text: ")
        response = bot.send_text(text)
        response_text = bot.get_text_response(response)
        driver.say(response_text)
    except DialogFailed:
        driver.say("Disculpa, no te entendí")
        continue
