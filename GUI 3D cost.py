from tkinter import *
from tkinter import ttk #

GUI = Tk()
GUI.geometry ('800x800')
GUI.title ('โปรแกรมคำนวนต้นทุนชิ้นงาน 3D print')
#####################################################################
A = Label(GUI, text = 'ราคาfilament ต่อม้วน 1KG',font = ('Angsana New',30))
A.pack()

v_costperfilament = StringVar() # ตัวแปรพิเสษเก็บข้อมูลใน GUI
A1 = Entry(GUI,textvariable=v_costperfilament ,font = ('Angsana New',20))
A1.pack()
####################################################################


B = Label(GUI, text = 'ความยาวต่อม้วน(เมตร)',font = ('Angsana New',30))
B.pack()

v_rawlenght = StringVar()
B1 = Entry(GUI,textvariable = v_rawlenght, font = ('Angsana New',20))
B1.pack()
######################################################################
C = Label(GUI, text = 'ความยาวที่ใช้ในการพิมพ์(เมตร)',font = ('Angsana New',30))
C.pack()

v_uselenght = StringVar()
C1 = Entry(GUI,textvariable = v_uselenght,font = ('Angsana New',20))
C1.pack()
#######################################################################
D = Label(GUI, text = 'เวลาที่ใช้ในการพิมพ์ (ช.ม.)',font = ('Angsana New',30))
D.pack()

v_time =  StringVar()
D1 = ttk.Entry(GUI,textvariable= v_time,font = ('Angsana New',20))
D1.pack()
########################################################################
D = Label(GUI, text = 'เครื่องพิมพ์กินไฟกี่วัตต์',font = ('Angsana New',30))
D.pack()

v_watt = StringVar()
D1 = ttk.Entry(GUI,textvariable = v_watt ,font = ('Angsana New',20))
D1.pack(pady=10)# pady เว้นระยะ
#####################################################################
def Caltotalcost():
    cost = float(v_costperfilament.get())
    lenght= float(v_rawlenght.get())
    uselenght = float(v_uselenght.get())
    time =  float(v_time.get())
    watt = float(v_watt.get())
    unit = 4.30
    electric = watt/1000* time * unit
    price = cost /lenght * uselenght
    totalprice = price + electric  
    print('Total cost:Baht',totalprice)
    text = 'ต้นทุนชิ้นงานรวม{:,.2f}บาท ค่าวัสดุ{:,.2f}บาท ค่าไฟ{:,.2f}บาท'.format(totalprice,price,electric)
    v_result.set(text)
###############################SHOWRESULT text####################################
v_result = StringVar()
result = ttk.Label(GUI,textvariable = v_result,font = ('Angsana New',20,'bold'),foreground = 'green')
result.pack(pady = 20)
#############################Botton######################################
E1 = ttk.Button(GUI,text ='CALCUlATE', width = 20, command = Caltotalcost )
E1.place(x = 330,y=600)

#######################################################################


GUI.mainloop()