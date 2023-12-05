import telebot

chave_api = "YOPUR-TOKEN"

bot = telebot.TeleBot(chave_api)# Open axie.live website and wait it to render JavaScript

bot.send_message(-123456, "teste python", reply_to_message_id=123)

