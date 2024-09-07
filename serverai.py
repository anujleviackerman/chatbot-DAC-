import socket
import time
import pickle
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template="""
answer the question below.

Here is the conversation history :{context}

Question:{question}


Answer:



"""

model=OllamaLLM(model='llama3')
prompt= ChatPromptTemplate.from_template(template)
chain= prompt | model
HEADERSIZE = 10
context=""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1242))
s.listen(7)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    msg = clientsocket.recv(1024).decode('utf8')
    print(msg)
    if msg.lower()=="exit":
        break
    else:
        result=chain.invoke({"context":context, "question": msg})
        clientsocket.send(result.encode('utf-8'))
        context += f"\nUser: {msg}\nAI: {result}"
    
            