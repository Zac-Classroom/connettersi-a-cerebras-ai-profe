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

domanda=input("come posso aiutarti?")
risposta = llm.invoke(domanda)

print(risposta.content)