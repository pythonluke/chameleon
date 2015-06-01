from tkinter import *
import time
import _thread
def close(self):
    self.frame.destroy()
def debugy(error,dictl):
    #print ("debugging")
    
    #print (dictl)
    count = 0
    global name
    #print (error)
    error = error.replace('\n', '~').replace('\r', '~') + "   "
    
    tok = ""
    file = 0
    line = 0
    arg = ""
    filefound = 0
    curline = ""
    errorline = -2
    fileline = 0
    while count < len(error):
        #print (error[count])
        curline = error[count]
        #print (errorline)
        

        tok = tok + error[count]
        #print ("indice")
        #print (tok)
        #print (tok)
        if error[count] == " " or error[count] == "\\" or error[count] == "\"":
            tok = ""
        if tok == "File":
            file = 1
            fileline = count - 4
        if error[count] == "~":
            file = 0
            curline = ""
            errorline = errorline - 1
            #print ("found new line")
        if file == 1 and not dictl.get(tok) == None:
            filefound = 1
            #print ("filefoundfffffffffffffffffffffffffffffffffffffffffffff")
            name = tok[:]
        if filefound == 1 and tok == "line":
            line = 1
            #print ("line")
        if line == 1:
            #print ("linelllllllllllllllllllllllllllllllllllllllllll")
            arg = arg + error[count]
        if error[count] == "," and filefound == 1 and line == 1:
            line = 0
            #print ("numbernnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
            #print (arg[2:-1])
            arg = arg[2:-1]
            arg = int(arg)
            dicty = dictl.get(name)
            print ("Chameleon error\n----------------------------------------")
            print ("File: " + name + ".cham, on line: " + str(dicty.get(arg)))
            print (getline(int(dicty.get(arg))))
            file = 0
            filefound = 0
            errorline = 3
            
            #print ("error")
            #print (error)
            error = error[:fileline] + "not valid error:~" + error[fileline + 1:]
            fileline = 0
            arg = ""
        if errorline == 1:
            arg = arg + error[count]
        if errorline == 0:
            print (arg.replace("~","\n"))
            errorline = -1
        count = count + 1
    print ("\n\nPython error\n----------------------------------------")
    print (error.replace("~","\n"))
def getline(line):
    global name
    name = name + ".cham"
    code = open(name,"r")
    code = code.read().replace("\n","~")
    cline = 1
    foundline = False
    i = 0
    arg = ""
    while i < len(code):
        if code[i] == "~":
            cline = cline + 1
        if cline == line:
            foundline = True
        if foundline:
            arg = arg + code[i]
        if cline == line + 1:
            return arg.replace("~","\n")
            break
        i = i + 1
timer1 = 0
rect = {}
    
class Game(Tk,Canvas,Button):
    def __init__(self):
        pass
    def frame(self,title,size):
        global frame
        global canvas
        
        self.frame = Tk()
        
        self.frame.title(title)
        geosize = str(size[0]) + "x" + str(size[1])
        self.frame.geometry(geosize)
        self.canvas = Canvas(self.frame, width = size[0], height = size[1])
        self.canvas.pack()

        self.frame.bind('<Configure>', self._resize_canvas)

 
    def resizable(self,x,y):
        self.frame.resizable(width=x,height=y)
    def _resize_canvas(self,event):
        

        new_width = event.width
        new_height = event.height
        self.canvas.config(width = new_width,height=new_height)

    def eventloop(self):
        self.frame.mainloop()
        
    def RectSprite(self,master,x,y,Width,Height,color):
        global sprite
        global width
        global height
        
        global y1
        global x1
        self.x1 = x
        self.y1 = y

        
        self.width = Width
        self.height = Height
        self.sprite = master.canvas.create_rectangle(x,y,x + self.width,y + self.height,fill=color)
    def position(self,master,x,y):
        global y1
        global x1
        self.x1 = x
        self.y1 = y
        master.canvas.coords(self.sprite,self.x1,self.y1,self.x1 + self.width,self.y1 + self.height)
        
    def SmoveX(self,master,x):
        global x1
        self.x1 += x
        master.canvas.coords(self.sprite,self.x1,self.y1,self.width,self.height)
    def SBmoveX(self,master,x):
        global x1
        self.x1 = self.x1 + x
        rectang = rect[self]
        rect[self] = [rectang[0] + x,rectang[1],rectang[2],rectang[3]]
        master.canvas.coords(self.sprite,self.x1,self.y1,self.width + self.x1,self.height + self.y1)
    def SmoveY(self,master,x):
        global y1
        self.y1 = self.y1 + x
        master.canvas.coords(self.sprite,self.x1,self.y1,self.width + self.x1,self.height)
    def SBmoveY(self,master,x):
        global x1
        self.y1 = self.y1 + x
        rectang = rect[self]
        rect[self] = [rectang[0],rectang[1] + x,rectang[2],rectang[3]]
        master.canvas.coords(self.sprite,self.x1,self.y1,self.width + self.x1,self.height + self.y1)

    def Cpos(self):
        return[self.x1,self.y1]
    
        
    def body(self,x1,y1,width,height):
        global rect
        rect[self] = [x1,y1,width,height]
    def touching(self,other):
        selfr = rect[self]
        otherr = rect[other]
        if selfr[0] >= otherr[0]:
            #is to the right
            if selfr[0] <= otherr[0] + otherr[2]:
                #are touching in the x direction
                if selfr[1] >= otherr[1]:
                    #is underneath
                    if selfr[1] <= otherr[1] + otherr[3]:
                        #is touching
                        return True
                    else:
                        return False
                else:
                    #is underneath
                    if selfr[1] + selfr[3] >= otherr[1]:
                        #is touching
                        return True
                    else:
                        return False
            else:
                return False
        else:
            #is to the left
            if selfr[0] + selfr[2] >= otherr[0]:
                #are touching in the x direction
                if selfr[1] >= otherr[1]:
                    #is underneath
                    if selfr[1] <= otherr[1] + otherr[3]:
                        #is touching
                        return True
                    else:
                        return False
                else:
                    #is underneath
                    if selfr[1] + selfr[3] >= otherr[1]:
                        #is touching
                        return True
                    else:
                        return False
            else:
                return False



    




         



