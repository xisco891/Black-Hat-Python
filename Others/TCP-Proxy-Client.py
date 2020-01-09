import socket 
import os
import threading 



def handle_client(client):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = client.recv(4096)
    print("A new message has been received :", response)
    

def main():
    
    client, addre = server.accept()
    client_instance = threading.Thread(target = handle_client, args=[client]
    client_instance.start()
    


