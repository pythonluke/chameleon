from debug import *

import traceback
try:
    import time 
    import random 
    import _thread 
    from tkinter import * 
    def loop(v,h):
        upper1.SBmoveX(win,1) 
        lower1.SBmoveX(win,1) 
        upper2.SBmoveX(win,1) 
        lower2.SBmoveX(win,1) 
        up1 = upper1.Cpos() 
        up2 = upper2.Cpos() 
        if up1[0] > 380 :
            upper1.SBmoveX(win,-380) 
            lower1.SBmoveX(win,-380) 
        elif up2[0] > 380 :
            upper2.SBmoveX(win,-380) 
            lower2.SBmoveX(win,-380) 
        if upper1.touching(bird) or lower1.touching(bird) :
            close(win) 
        if upper2.touching(bird) or lower2.touching(bird) :
            close(win) 
    def main(h,v) :
        global fps 
        fps = 60 
        while True :
            _thread.start_new_thread( loop,(1,1,) )
            time.sleep(1 / fps) 
    win = Game() 
    win.frame("Flappy Bird",(400,400)) 
    win.resizable( False , False ) 
    bird = Game() 
    bird.RectSprite(win,350,30,30,30,"yellow") 
    bird.body(350,30,30,30) 
    upper1 = Game() 
    upper1.RectSprite(win,200,0,20,150,"black") 
    upper1.body(200,0,20,150) 
    lower1 = Game() 
    lower1.RectSprite(win,200,250,20,150,"black") 
    lower1.body(200,250,20,150) 
    upper2 = Game() 
    upper2.RectSprite(win,0,0,20,150,"black") 
    upper2.body(0,0,20,150) 
    lower2 = Game() 
    lower2.RectSprite(win,0,250,20,150,"black") 
    lower2.body(0,250,20,150) 
    _thread.start_new_thread( main,(1,1,) )
    win.eventloop() 
except Exception: 
    exc_info = traceback.format_exc()
    di = {'helloworld': {5: 1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6, 11: 7, 12: 9, 13: 10, 14: 12, 15: 13, 16: 14, 17: 15, 18: 16, 19: 18, 20: 19, 21: 20, 22: 22, 23: 23, 24: 26, 25: 27, 26: 34, 27: 35, 28: 36, 29: 38, 30: 39, 31: 40, 32: 43, 33: 44, 34: 45, 35: 47, 36: 48, 37: 49, 38: 52, 39: 53, 40: 54, 41: 56, 42: 57, 43: 58, 44: 61, 45: 62, 46: 63, 47: 65, 48: 66, 49: 67, 50: 69, 51: 71}}
    debugy(exc_info,di)
    x = input("")