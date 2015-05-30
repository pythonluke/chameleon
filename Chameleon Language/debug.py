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

