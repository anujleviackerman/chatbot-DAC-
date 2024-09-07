import socket
import time
import pickle
import pandas as pd
import os


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(7)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    x=True
    while x:
        full_msg = b''
        new_msg = True
        while True:
            msg = clientsocket.recv(16)
            if new_msg:
                print("new msg len:",msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            print(f"full message length: {msglen}")

            full_msg += msg

            print(len(full_msg))

            if len(full_msg)-HEADERSIZE == msglen:
                print("full msg recvd")
                print(full_msg[HEADERSIZE:])
                dictionary=pickle.loads(full_msg[HEADERSIZE:])
                print(dictionary)
                if dictionary["code_from"]=="reg":
                    print("reg")
                    new_data = [dictionary["username"],dictionary["email"],dictionary["password"]]
                    print(new_data)
                    csv_file_path = 'Book2.csv'
                    df = pd.DataFrame([new_data])
                    df.to_csv(csv_file_path, mode='a', header=False, index=False)
                    print(f'Unique data has been appended to {csv_file_path}')

                elif dictionary["code_from"]=="login":
                    csv_file_path="Book2.csv"
                    df=pd.read_csv(csv_file_path)
                    emial_column='email'
                    is_present_email= dictionary["email"] in df[emial_column].values
                    csv_file_path="Book2.csv"
                    df=pd.read_csv(csv_file_path)
                    password_column='password'
                    is_present_password= dictionary["password"] in df[password_column].values
                    if is_present_email==True and is_present_password==True:
                        final="True"
                        clientsocket.send(final.encode('utf-8'))
                    else:
                        final="False"
                        clientsocket.send(final.encode('utf-8'))
                x=False
                break
