# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:35:20 2024

@author: Aidan
"""

from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time


root=Tk()
root.geometry("600x600")
spain_image = ImageTk.PhotoImage(Image.open ("mapa-españa.jpg"))
mexico_image = ImageTk.PhotoImage(Image.open ("Mapa_mexico.jpg"))
#-----------------India-----------------
mexico_label = Label(root,text="Mexico")
mexico_label.place(relx=0.2,rely=0.05, anchor= CENTER)


mexico_clock=Label(root)
mexico_clock["image"]=mexico_image
mexico_clock.place(relx=0.2,rely=0.35, anchor= CENTER)




mexico_time = Label(root)
mexico_time.place(relx=0.2,rely=0.65, anchor= CENTER)
#-----------------------US---------------
españa_label = Label(root,text="España")
españa_label.place(relx=0.7,rely=0.05,anchor= CENTER)


españa_clock=Label(root)
españa_clock.place(relx=0.7,rely=0.35, anchor= CENTER)
españa_clock["image"]=clock_image


españa_time = Label(root)
españa_time.place(relx=0.7,rely=0.65, anchor= CENTER)


class Mexico():
    def times(self):
        home=pytz.timezone('America/central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        mexico_time["text"]="Time :"+ current_time
        mexico_time.after(200,self.times)
class España():
    def times(self):
        home=pytz.timezone('Spain/Madrid')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        españa_time["text"]="Time :"+ current_time
        españa_time.after(200,self.times)
       
obj_mexico=Mexico()
obj_españa=España()
mexico_btn=Button(root,text="Show Time",command=obj_india.times)
mexico_btn.place(relx=0.2,rely=0.8, anchor= CENTER)
españa_btn=Button(root,text="Show Time",command=obj_usa.times)
españa_btn.place(relx=0.7,rely=0.8, anchor= CENTER)
root.mainloop()

