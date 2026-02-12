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

memoria={}
formato_memoria= "DOMANDA: {prompt}; RISPOSTA: {risposta}"

istruzioni=""" 
sei un assistente arrabbiatissimo che parla anche piu lingue se rischiesto e insulta tutti e risponde alle domande anche sulla base delle conversazioni precedenti, poste di seguito

CONVERSAZIONI PRECEDENTI:
{memoria}
DOMANDA: {prompt}
"""
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    user_id= message.from_user.id
    prompt=message.text

    if user_id in memoria:
        conversazioni=memoria[user_id]
    else:
        conversazioni=""""""

    conversazioni=memoria.get(user_id, [])
    istruzioni_formattate=istruzioni.format(memoria=conversazioni, prompt=prompt)

    risposta=llm.invoke(istruzioni_formattate)

    if not user_id in memoria:
        memoria[user_id]=[]

    memoria[user_id].append(formato_memoria.format(prompt=prompt, risposta=risposta.content))
    bot.reply_to(message, f"{risposta.content}")
bot.polling()