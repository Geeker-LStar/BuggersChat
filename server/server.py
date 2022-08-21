import tkinter as tk
import time
import socket
import threading
from l10n import *

lang = "zh-CN"
# lang="en-US"

# 服务端发送的消息
def Send_Message():
    result = GulSlk.get("1.0", "end")
    sock.send(result.encode())
    theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    GulListBox.insert("end", get_str("server",lang) + "     " + theTime + ":")
    GulListBox.insert("end", "             " + result)
    GulSlk.delete("1.0", "end")
 
# 接收客户端消息
def Receive_Client(sock,addr):
    while True:
        info=sock.recv(1024).decode()
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        GulListBox.insert("end", get_str("client",lang) + "     " + theTime + ":")
        GulListBox.insert("end", "             " + info)

def Sever_init(sock,addr):
    print(get_str("successful_connection",lang))
    Threading_one = threading.Thread(target=Receive_Client, args=(sock,addr))
    Threading_one.daemon = True
    Threading_one.start()
 
if __name__ == '__main__':
    window = tk.Tk()
 
    window.geometry('600x600')
    window.title(get_str("window_title",lang))
 
    GulListBox = tk.Listbox(window, width=120, height=20)
    GulListBox.pack()
 
    GulButton = tk.Button(window, width=10, text=get_str("send",lang), command=Send_Message)
    GulButton.place(x=500, y=550)
 
    GulSlk = tk.Text(window, width=120, height=10)
    GulSlk.place(x=10, y=400)
 
    host = socket.gethostname()
    post = 1320
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, post))
    s.listen(2)
 
    print(get_str("waiting_for_connection",lang))
    sock, addr = s.accept()
 
    threading1=threading.Thread(target=Sever_init,args=(sock,addr))
    threading1.start()
 
    window.mainloop()
