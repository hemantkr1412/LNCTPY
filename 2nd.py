# 
# 
from tkinter import * 
from tkinter.ttk import *

win= Tk() 
win.geometry('200x200') 
v = StringVar(win, "1") 

# we will add Style class to add style to Radiobutton  
style = Style(win) 
style.configure("TRadiobutton", background = "light blue", 
				foreground = "orange", font = ("arial", 14, "bold")) 

# Dictionary to create multiple buttons 
values = {"RadioButton 1" : "1", 
		"RadioButton 2" : "2", 
		"RadioButton 3" : "3" 
		} 

for (text, value) in values.items(): 
	Radiobutton(win, text = text, variable = v, 
				value = value).pack(side = TOP, ipady = 3) 
mainloop() 