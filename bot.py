from dotenv import dotenv_values
import telebot

config = dotenv_values(".env")

print (config)

bot = telebot.TeleBot(config["telegram"])

@bot.message_handler(func = lambda message: True)
def echo__message(message):
    print (message)
    bot.reply_to(message, "Si sono il miglior Dj della Puglia")

bot.polling()