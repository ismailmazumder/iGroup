import os,socket
from concurrent.futures import thread
from tkinter import Tk, Label
from threading import Thread
ip = "127.0.0.1"
port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip,port))

conn_list = []
user_name = []
message = ''
def main():
    server.listen()
    while True:
        conn , addr = server.accept()
        conn_list.append(conn)
        name = conn.recv(1029).decode('ascii')
        print(conn,name)
        thread_main = Thread(target=recieve,args=(conn,))
        thread_main.start()
def recieve(conn):
    while True:
        print(conn)
        message = conn.recv(1040).decode('ascii')
        print(message)
        #new
        all_send(message)
def all_send(message):
    for conn_trans in conn_list:
        conn_trans.send(message.strip("user_message_88792222222").encode("ascii"))
main()