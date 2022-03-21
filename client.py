import tkinter,os
from tkinter import filedialog, END

try:
    import customtkinter
except:
    os.system("pip install customtkinter")
    import customtkinter
import socket
try:
    from win32api import GetSystemMetrics
except:
    pass
from threading import Thread
ip = "3.131.147.49"
port = 10421
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((ip,port))
root = customtkinter.CTk()
try:
    root.geometry(f"{GetSystemMetrics(0)}x{GetSystemMetrics(1)}")
except:
    pass
try:
    root.iconbitmap('dolby.ico')
except:
    pass
user_name_ = ''
root.title('iGroup')
def main():
    user_name = customtkinter.CTkEntry(root,width=900)
    user_name.pack()
    def send_user_name():
        global user_name_
        user_name_text = user_name.get()
        user_name_ = user_name_text
        print(user_name_text)
        server.send(user_name_text.encode('ascii'))
        user_name.destroy()
        submit_button.destroy()
        user_message = customtkinter.CTkEntry(root,width=500)

        user_message.pack()
        def recieve():
            while True:
                server_message = server.recv(1029).decode('ascii')
                show = customtkinter.CTkLabel(text=server_message)
                show.pack()
                #emoji show
                if server_message == 'emoji_1' or server_message == 'oji_1':
                    emoji = tkinter.PhotoImage(file='2.png')
                    show_image = customtkinter.CTkLabel(root, image=emoji)
                    show_image.pack(side=tkinter.LEFT)
        recieve_thread = Thread(target=recieve)
        recieve_thread.start()
        file_select_text = "Choose file"
        def attach_file():
            global file_select_text
            file = filedialog.askopenfilename()
            file_select_text = file
            print(file_select_text)
            file_choose_button.pack()
        file_choose_button = customtkinter.CTkButton(root,text = file_select_text,command=attach_file)
        file_choose_button.pack()
        # emoji
        def emoji():
            server.send("emoji_1".encode('ascii'))
        image_1 = tkinter.PhotoImage(file='2.png')
        now_path = os.getcwd()
        emoji_button = customtkinter.CTkButton(root,image =image_1,command=emoji)
        emoji_button.pack()
        #send o korte hbe
        def send_user_message():
            final_message = user_message.get()
            print(final_message)
            print(type(final_message))
            server.send(f"{user_name_} : {final_message}".encode('ascii'))
            user_message.delete(0, END)
            user_message_show = customtkinter.CTkLabel(text=user_message.get())
            #user_message_show.pack()
        send_user_message_button = customtkinter.CTkButton(text='SEND',command=send_user_message)
        send_user_message_button.pack()
    submit_button = customtkinter.CTkButton(text='SUBMIT',command=send_user_name)
    submit_button.pack()
main()
root.mainloop()
