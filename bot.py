from dotenv import dotenv_values
import telebot
from langchain.chat_models import init_chat_model

config=dotenv_values(".env")
print(config)

bot= telebot.TeleBot(config["telegram"])

llm = init_chat_model(config['MODEL']
        , temperature= config['TEMPERATURE']
        , api_key= config['key']
        , verbose= True
        , base_url= "https://api.cerebras.ai/v1/") #indirizzo del server di cerebras 

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    user_id= message.from_user.id
    prompt=message.text

    risposta=llm.invoke(prompt)

    bot.reply_to(message, f"la risposta è: {risposta.content}")

bot.polling()