from translate import *
import time
transfile = []
run = []
debug = []
j = "y"
while j == "y":
    x = input("the name of the file you want to translate\n")
    transfile.append(x)
    r = input("do you want to run this file 1 or 0\n")
    run.append(int(r))
    debug.append(1)
    j = input("another file y or n\n")
pause = input("do want to have to press enter between runs y or n\n")
while 1 == 1:
    print (run)
    py(transfile,debug,run)
    if pause == "y":
        p = input("")
        print ("translate----------------------------------------------")
    
    
