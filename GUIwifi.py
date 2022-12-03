from tkinter import *
import socket
import threading
import time
def runserver():
    #####################
    serverip = '192.168.1.8'
    port = 9000
    #####################

    buffsize = 4096

    while True:
            server = socket.socket()
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            server.bind((serverip,port))
            server.listen(1)
            print('waiting micropython...')

            client, addr = server.accept()
            print('connected from:', addr)

            data = client.recv(buffsize).decode('utf-8')
            print('Data from MicroPython: ',data)
            # data= 'LED1:ON/'LED1:OFF'
            data_split = data.split(':')
            if data_split[1] == 'ON':
                V_status.set('{} status {}'.format(data_split[0],data_split[1]))
                L2.configure(fg='green')
                time.sleep(1)
            else:
                V_status.set('{} status {}'.format(data_split[0],data_split[1]))
                L2.configure(fg='red')
                time.sleep(1)
            client.send('received your messages.'.encode('utf-8'))
            client.close()



GUI = Tk()
GUI.geometry('600x600')
GUI.title('IOT status by PKRAOMING')

FONT = ( 'Angsana New',30)


L1 = Label(GUI,text=' LED status from micropython',font=FONT)
L1.pack()


V_status = StringVar()
V_status.set('<<< No status>>>')
L2 = Label(GUI,textvariable=V_status,font=FONT)
L2.configure(fg= 'red')
L2.pack()


#############runserver#############
task = threading.Thread(target=runserver)
task.start()
##################################


GUI.mainloop()
