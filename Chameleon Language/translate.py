#file = open("hello.py","w")
#x = "print (\"hello\")"
#file.write(x)
#file.close()
import subprocess
def py(filname,debugi,runi):
    fdict = {}
    for filename in filname:   
        x = open(filename + ".cham","r")
        x = x.read().replace("\n", " ~ ")
        tok = ""
        end = 0
        count = 0
        x = x + " "
        output = ""
        printy = 0
        runy = 0
        arg = ""
        fory = 0
        forarg = 0
        y = ""
        var = 0
        indent = ""
        ify = 0
        ifarg = 0
        elsey = 0
        elsearg = 0
        elify = 0
        elifarg = 0
        whiley = 0
        whilearg = 0
        funcy = 0
        funcarg = 0
        returny = 0
        importy = 0
        fromy = 0
        thry = 0
        tryy = 0
        tryarg = 0
        excepty = 0
        exceptarg = 0
        classy = 0
        classarg = 0
        string = -1
        lock = 0
        line = 1
        lcom = 0
        com = 0
        ldict = {}
        
        
        indent = "    "
        pyline = 5
        while count < len(x):
            tok = tok + x[count]
            #print (indent + "15")
            #print (line)
            print (tok)
            #print (com)
            #print (lcom)
            
            if x[count] == "\"":
                if x[count - 2] + x[count - 1] == "\\\\":
                    string = string * -1
                if not x[count - 1] == "\\":
                    string = string * - 1
            if x[count] == "~":
                line = line + 1
                
                if lcom == 1:
                    string = -1
                lcom = 0
            if x[count] == " ":
                
                tok = ""
            if x[count] == "    ":
                tok = ""
                
            if x[count] == "#" and string == -1:
                lcom = 1
            if tok == "/*" and string == -1:
                com = 1
            if com == 1 and tok == "*/":
                com = 0
                string = -1
            if com == 1 or lcom == 1:
                string = 1
            if printy == 1 and x[count - 1] == ";" and not x[count - 2] == "//" and string == -1:
                printy = 0
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                #print ("running")
                y = y + indent + "print (" + arg[1:-1] + ")\n"
                #print (y)
                lock = lock - 1
            if var == 1 and x[count - 1] == ";" and not x[count - 2] == "//" and string == -1:
                var = 0
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                #print ("var")
                #print (arg[1:-1])
                y = y + indent + arg[1:-1] + "\n"
                #print (y)
                lock = lock - 1
            if runy == 1 and x[count - 1] == ";" and not x[count - 2] == "//" and string == -1:
                runy = 0
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                #print ("running")
                y = y + indent + arg[1:-1] + "\n"
                #print (y)
                lock = lock - 1
            if returny == 1 and x[count - 1] == ";" and not x[count - 2] == "//" and string == -1:
                returny = 0
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                #print ("running")
                y = y + indent + "return" + arg[1:-1] + "\n"
                #print (y)
                lock = lock - 1
            if fromy == 1 and x[count - 1] == ";" and not x[count - 2] == "//" and string == -1:
                fromy = 0
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                #print ("running")
                y = y + indent + "from" + arg[:-1] + "\n"
                #print (y)
                lock = lock - 1
            if importy == 1 and x[count - 1] == ";" and not x[count - 2] == "//" and string == -1:
                importy = 0
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                #print ("running")
                y = y + indent + "import" + arg[:-1] + "\n"
                #print (y)
                lock = lock - 1
            if thry == 1 and x[count - 1] == ";" and not x[count - 2] == "//" and string == -1:
                thry = 0
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                #print ("running")
                y = y + indent + "_thread.start_new_thread" + "(" + arg[:-1] + ")\n"
                #print (y)
                lock = lock - 1   
            if printy == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if runy == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if returny == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if fromy == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if importy == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if var == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if ifarg == 0 and ify == 1 and tok == "}if" and not x[count - 1] == "\\" and string == -1:
                ify = 0
                #print ("indent first")
                #print (indent + "1")
                indent = indent[:-4]
                #print ("indent after")
                #print (indent + "1")
                #print (y)
            elif elsearg == 0 and elsey == 1 and tok == "}else" and not x[count - 1] == "\\" and string == -1:
                elsey = 0
                #print ("s")
                indent = indent[:-4]
            elif tryarg == 0 and tryy == 1 and tok == "}try" and not x[count - 1] == "\\" and string == -1:
                tryy = 0
                #print ("s")
                indent = indent[:-4]
            elif elifarg == 0 and elify == 1 and tok == "}elif"and not x[count - 1] == "\\" and string == -1:
                elify = 0
                #print ("f")
                indent = indent[:-4]
            elif whilearg == 0 and whiley == 1 and tok == "}while" and not x[count - 1] == "\\" and string == -1:
                whiley = 0
                #print ("z")
                indent = indent[:-4]
            elif forarg == 0 and fory == 1 and tok == "}for" and not x[count - 1] == "\\" and string == -1:
                fory = 0
                #print ("z")
                indent = indent[:-4]  
                print ("for loop ended")
            elif funcarg == 0 and funcy == 1 and tok == "}func" and not x[count - 1] == "\\" and string == -1:
                funcy = 0
                #print ("h")
                indent = indent[:-4]
            elif classarg == 0 and classy == 1 and tok == "}class" and not x[count - 1] == "\\" and string == -1:
                classy = 0
                #print ("h")
                indent = indent[:-4]
            elif exceptarg == 0 and excepty == 1 and tok == "}except" and not x[count - 1] == "\\" and string == -1:
                excepty = 0
                #print ("h")
                indent = indent[:-4]
     
            if elsearg == 1 and elsey == 1 and x[count - 1] == "{" and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                elsearg = 0
                #print ("arg")
                #print (arg[:-1])
                y = y + indent + "else" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""
            if tryarg == 1 and tryy == 1 and x[count - 1] == "{" and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1            
                tryarg = 0
                #print ("arg")
                #print (arg[:-1])
                y = y + indent + "try" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""
            if elifarg == 1 and elify == 1 and x[count - 1] == "{" and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1            
                elifarg = 0
                #print ("arg")
                #print (arg[:-1])
                y = y + indent + "elif" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""
            if whilearg == 1 and whiley == 1 and x[count - 1] == "{" and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                whilearg = 0
                #print ("while")
                #print (arg[:-1])
                y = y + indent + "while" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""  
            if forarg == 1 and fory == 1 and x[count - 1] == "{" and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1
                forarg = 0
                #print ("while")
                #print (arg[:-1])
                y = y + indent + "for" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""      
                print ("for loop evaluate::::::::::::::::::::::::::::::::::::::::::::::::::::")
            if ifarg == 1 and ify == 1 and x[count - 1] == "{" and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1           
                ifarg = 0
                #print ("arg")
                
                #print (arg[:-1])
                y = y + indent + "if" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""
            if funcarg == 1 and funcy == 1 and x[count - 1] == "{"  and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1            
                funcarg = 0
                #print ("arg")
                
                #print (arg[:-1])
                y = y + indent + "def" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""
            if classarg == 1 and classy == 1 and x[count] == "{" and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1            
                classarg = 0
                #print ("arg")
                
                #print (arg[:-1])
                y = y + indent + "class" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""

            if exceptarg == 1 and excepty == 1 and x[count - 1] == "{" and not x[count - 2] == "\\" and string == -1:
                ldict[pyline] = line
                print (ldict)
                pyline = pyline + 1            
                exceptarg = 0
                #print ("arg")
                
                #print (arg[:-1])
                y = y + indent + "except" + arg[:-1] + ":\n"
                indent = indent + "    "
                arg = ""  
            if ifarg == 1 and ify == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            
            if elsearg == 1 and elsey == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if tryarg == 1 and tryy == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if elifarg == 1 and elify == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                   arg = arg + x[count] 
            if whilearg == 1 and whiley == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if forarg == 1 and fory == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]                    
            if funcarg == 1 and funcy == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if classarg == 1 and classy == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if exceptarg == 1 and excepty == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                else:
                    arg = arg + x[count]
            if thry == 1:
                if x[count] == "\"":
                    arg = arg + "\""
                elif x[count] == "^":
                    arg = arg + "\n"
                elif x[count] == "\\":
                    arg = arg + "\\"
                elif x[count] == "(":
                    arg = arg + ",("
                elif  x[count] == ")":
                    arg = arg + ",)"
                else:
                    arg = arg + x[count]
            if tok == "print" and string == -1:
                #print ("print")
                #print (lock)
                if lock == 0:
                    printy = 1
                    arg = ""
                    lock = lock + 1
                else:
                    print ("SyntaxError: missing ; at line nimber:" + str(line))
                    y = input("close the program")
                    end = 1
                    break
            if tok == "var" and string == -1:
                #print ("lock")
                #print (lock)
                if lock == 0:
                    #print("var")
                    var = 1
                    arg = ""
                    lock = lock + 1
                else:
                    print ("SyntaxError: missing ; at line nimber:" + str(line))
                    y = input("close the program")
                    end = 1
                    break
            if tok == "if" and string == -1:
                ify = 1
                ifarg = 1
                arg = ""
                
            if tok == "else" and string == -1:
                elsey = 1
                elsearg = 1
                arg = ""
            if tok == "try" and string == -1:
                tryy = 1
                tryarg = 1
                arg = ""
            if tok == "elif" and string == -1:
                elify = 1
                elifarg = 1
                arg = ""
            if tok == "while" and string == -1:
                whiley = 1
                whilearg = 1
                arg = ""
            if tok == "for" and string == -1:
                fory = 1
                forarg = 1
                arg = ""   
                print ("for loop")
            if tok == "func" and string == -1:
                funcy = 1
                funcarg = 1
                arg = ""
            if tok == "class" and string == -1:
                classy = 1
                classarg = 1
                arg = ""
            if tok == "except" and string == -1:
                excepty = 1
                exceptarg = 1
                arg = ""
            if tok == "run" and string == -1:
                if lock == 0:
                    runy = 1
                    arg = ""
                    lock = lock + 1
                else:
                    print ("SyntaxError: missing ; at line :" + str(line))
                    y = input("close the program")
                    end = 1
                    break
            if tok == "return" and string == -1:
                if lock == 0:
                    returny = 1
                    arg = ""
                    lock = lock + 1
                else:
                    print ("SyntaxError: missing ; at line :" + str(line))
                    y = input("close the program")
                    end = 1
                    break
            if tok == "from" and string == -1:
                if lock == 0:
                    fromy = 1
                    arg = ""
                    lock = lock + 1
                else:
                    print ("SyntaxError: missing ; at line :" + str(line))
                    y = input("close the program")
                    end = 1
                    break           
            if tok == "import" and fromy == 0 and string == -1:
                if lock == 0:
                    importy = 1
                    arg = ""
                    lock = lock + 1
                else:
                    print ("SyntaxError: missing ; at line :" + str(line))
                    y = input("close the program")
                    end = 1
                    break
            if tok == "thr" and string == -1:
                if lock == 0:
                    thry = 1
                    arg = ""
                    lock = lock + 1
                else:
                    print ("SyntaxError: missing ; at line :" + str(line))
                    y = input("close the program")
                    end = 1
                    break
            
                
            count = count + 1
        fdict[filename] = ldict
        ldict = {}
        debug = 1
        if end == 0:
            if debug == 1:
                y = "from debug import *\n\nimport traceback\ntry:\n" + y + "except Exception: \n    exc_info = traceback.format_exc()\n    di = " + str(fdict) + "\n    debugy(exc_info,di)\n    x = input(\"\")"  
            z = open(filename + ".py","w")
            z.write(y)
            z.close()
            #print (y)
            print ("translated------------------------------------------")
    for i in range(len(runi)):
        run = runi[i]
        filename = filname[i]
        if run == 1 and end == 0:
            subprocess.call(["C:\\Python34\\python.exe",filename + ".py"])
def html(name,filename,run):

    l = 0
    x = open(filename,"r")
    x = x.read().replace("\n", " \n ")
    x = x + " "
    tok = ""
    count = 0
    title = 0
    header = 0
    arg = ""
    body = ""
    head = ""
    p = 0
    img = 0
    Button = 0
    string = -1
    #print (x)
    while count < len(x):

        tok = tok + x[count]
        if x[count] == "\"":
            if x[count - 2] + x[count - 1] == "\\\\":
                string = string * -1
            if not x[count - 1] == "\\":
                string = string * - 1
        ##print (count)
        #print ("hhh")
        #print (tok)
        ##print (title)
        ##print (str(header) + "header")
        ##print (p)
        ##print (l)
        if x[count] == " ":
            tok = ""
            
        if title == 1 and x[count] == ";" and string == -1:
            ##print ("t" + arg)
            head = head + "  <title" + arg + "</title>\n"
            arg = ""
            title = 0
        if header == 1 and x[count] == ";" and string == -1:
            ##print ("h" + arg)
            body = body + "  <h" + arg + "</h" + arg[:1] + ">\n"
            arg = ""
            header = 0
        if p == 1 and x[count] == ";" and string == -1:
            ##print ("p"+ arg)
            body = body + "  <p" + arg + "</p>\n"
            arg = ""
            p = 0
        if l == 1 and x[count] == ";" and string == -1:
            ##print ("link" + arg)
            ##print ("  <a" + arg + "</a>\n")
            body = body + "  <a" + arg + "</a>\n"
            arg = ""
            l = 0
        if img == 1 and x[count] == ";" and string == -1:
            ##print ("link" + arg)
            ##print ("  <a" + arg + "</a>\n")
            body = body + "  <img" + arg + "</img>\n"
            arg = ""
            img = 0
        if Button == 1 and x[count] == ";" and string == -1:
            ##print ("link" + arg)
            ##print ("  <a" + arg + "</a>\n")
            body = body + "  <button" + arg + "</button>\n"
            arg = ""
            Button = 0
        if title == 1:
            if x[count - 1] == "\\" and x[count] == ":":
                arg = arg + ":"
            elif x[count] == "^":
                arg = arg + "<br>"
            elif x[count] == "\\":
                arg = arg + "\\"
            elif x[count] == "\"":
                arg = arg + "\""
            elif x[count] == ":":
                arg = arg + ">"
            else:
                arg = arg + x[count]
        if header == 1:
            if x[count - 1] == "\\" and x[count] == ":":
                arg = arg + ":"
            elif x[count] == "^":
                arg = arg + "<br>"
            elif x[count] == "\\":
                arg = arg + "\\"
            elif x[count] == "\"":
                arg = arg + "\""
            elif x[count] == ":":
                arg = arg + ">"
            else:
                arg = arg + x[count]
        if p == 1:
            if x[count - 1] == "\\" and x[count] == ":":
                arg = arg + ":"
            elif x[count] == "^":
                arg = arg + "<br>"
            elif x[count] == "\\":
                arg = arg + "\\"
            elif x[count] == "\"":
                arg = arg + "\""
            elif x[count] == ":":
                arg = arg + ">"
            else:
                arg = arg + x[count]
        if l == 1:
            ##print ("arg")
            ##print (arg)
            if x[count - 1] == "\\" and x[count] == ":":
                arg = arg + ":"
            elif x[count] == "^":
                arg = arg + "<br>"
            elif x[count] == "\\":
                arg = arg + "\\"
            elif x[count] == "\"":
                arg = arg + "\""
            elif x[count] == ":":
                arg = arg + ">"
            else:
                arg = arg + x[count]
        if img == 1:
            ##print ("arg")
            ##print (arg)
            if x[count - 1] == "\\" and x[count] == ":":
                arg = arg + ":"
            elif x[count] == "^":
                arg = arg + "<br>"
            elif x[count] == "\\":
                arg = arg + "\\"
            elif x[count] == "\"":
                arg = arg + "\""
            elif x[count] == ":":
                arg = arg + ">"
            else:
                arg = arg + x[count]
        if Button == 1:
            ##print ("arg")
            ##print (arg)
            if x[count - 1] == "\\" and x[count] == ":" :
                arg = arg + ":"
            elif x[count] == "^":
                arg = arg + "<br>"
            elif x[count] == "\\":
                arg = arg + "\\"
            elif x[count] == "\"":
                arg = arg + "\""
            elif x[count] == ":":
                arg = arg + ">"
            else:
                arg = arg + x[count]
        if tok == "title" and string == -1:
            title = 1
            arg = ""
            #print ("t")
        
        if tok == "h"  and x[count + 2] == " " and string == -1:
            print ("1h")
            if count < len(x) - 1:
                print ("2h")
                if x[count + 1] == "1" or x[count + 1] == "2" or x[count + 1] == "3" or x[count + 1] == "4" or x[count + 1] == "5" or x[count + 1] == "6" :
                    print ("3h")
                    header = 1
                    arg = ""
                    print ("header")

        if tok == "p" and x[count + 1] == " " and string == -1:
            p = 1
            arg = ""
            #print ("p")
        
        if tok == "l" and x[count + 1] == " " and string == -1:
            l = 1
            #print ("link found")
            arg = ""
        if tok == "img" and x[count + 1] == " " and string == -1:
            img = 1
            #print ("link found")
            arg = ""
        if tok == "sep" and x[count + 1] == " " and string == -1:
            body = body + "  <hr>\n"
        if tok == "Button" and x[count + 1] == " " and string == -1:
            
            Button = 1
            arg = ""
        count = count + 1

    
    y = "<!doctype html>\n<html>\n  <head>\n" + head + "</head>\n<body>\n" + body + "</body>"
    
    print (y)
    z = open(name,"w")
    z.write(y)
    z.close()
    print ("translated")
    if run == 1:
        subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe","file:///C:/Users/lucas/Desktop/python/" +  name])
        
        
        
