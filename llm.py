from dotenv import dotenv_values
from langchain.chat_models import init_chat_model

config=dotenv_values(".env")

print(config)
print(config["MODEL"])

llm = init_chat_model(config['MODEL']
        , temperature= config['TEMPERATURE']
        , api_key= config['key']
        , verbose= True
        , base_url= "https://api.cerebras.ai/v1/") #indirizzo del server di cerebras 

risposta = llm.invoke("spiegami brevemente la funzione esponenziale")

print(type(risposta))

print(risposta)
print(risposta.content)