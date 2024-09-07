# chatbot-DAC-
a chatbot website using ollama
<br>
to make this chatbot ollama must be installed in ur computer 
also the env must be activated or the the following libraries must be installed
<br>
how does it work??
<br>
<br>
two servers server.py and serverai.py are running 
(server.py)-is the server that handles all the information regarding the details inputed by the client.It does it by using sockets to recv and transmit data as a dictionary and uses pandas to save and read the information to and from a csv file 
<br>
(serverai.py)-is the server that handles the input questions inputed by the client and processes the input question using llama and sends the result to client (clien.py) to be printed.It does it by using sockets to recv and transmit data as a dictionary
<br>
(client.py)-is the code that hosts and runs the website using flask and sockets to communicate with the servers 
