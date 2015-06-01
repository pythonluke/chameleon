from debug import *

import traceback
try:
    from tkinter import * 
    def move(event) :
        print ("hello" )
        label1.place(x=event.x,y=event.y) 
    win = Tk() 
    win.geometry("400x400") 
    win.title("Gui Builder") 
    label1 = Button(win, text="label") 
    win.bind("Key",move) 
    label1.place(x=10,y=10) 
    win.mainloop() 
    print ("hellooo" )
except Exception: 
    exc_info = traceback.format_exc()
    di = {'test': {5: 1, 6: 2, 7: 3, 8: 4, 9: 6, 10: 7, 11: 8, 12: 10, 13: 11, 14: 12, 15: 16, 16: 18}}
    debugy(exc_info,di)
    x = input("")