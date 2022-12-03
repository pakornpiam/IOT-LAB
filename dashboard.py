from tkinter import *
from PIL import Image,ImageTk
GUI = Tk()
GUI.geometry('900x600')
GUI.title('DASH BOARD IOT CONTROL SMART FARM')
###GUI.state('zoomed')    #make full screen


###test## 1234
canvas = Canvas(GUI,width=5000,height=900)
canvas.place(x=0,y=0)

background = ImageTk.PhotoImage(Image.open('farm2.png'))
canvas.create_image(100,200,anchor=NW,image=background)

#write squar ( polygon ) 
canvas.create_polygon([378,430,379,380,435,410,435,460],fill='green',outline='red')

GUI.mainloop()
