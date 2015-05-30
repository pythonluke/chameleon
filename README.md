# chameleon
chameleon is a new programming language that is python based. 
For sytax higlighting of chameleon dowload the texteditor notepad++.
Save the file called chameleon as a .xtml file.
Then click on lanuages , define your language, then import file.
Import the file called chameleon.

Now to create a new project you have to have python 3.4 installed.

So in notepad++ create a file with the file extension .cham, the file has to be saved in the chameleon folder.
We will make a simple HelloWorld program.

type:

print "Hello World!";

to execute the file open run chameleon.
It will ask you what file you want to run type your programs filename without the file extension and press enter.
Then it will ask you if you want to run the program type 1 to run.
Next it will ask you if you want to execute another file type n for no, if you had several chameleon files you would say yes, if you had several files
that are dependent on each other type you have to all compile then in the same process otherwise you woud not recieve proper error messages.
Finally it will ask you do you want to have to press space all the time between runs, say y otherwise the program will end and immediatly re run.
If you did this correctly you should get the result Hello World!.

When I say compile I mean it translates the chameleon to python code which the python interpreter can run so if you distribute 
the translated file which is always the filename + .py the user does not have to download any extra files.

Cheat Sheet:
Statements:
  end with ;
Single Line comments:
  start with #
Multi Line comments:
  start with /* and end with */
New line character:
  is ^
variables:
  are dynamic
  are strongly typed
  use the var keyword
  have to be set to a value or None
  list or arrays start with [ and end with ]
  dictionaries start with { and end with } keys are defined with : 
  tupples start with ( and end with ) and must have comma even with only one item
  user input is gotten with using the input () function
functions:
  are declared with the func keyword 
  arguments and name of function are defined befor the { character
  the end of a function is the keyword }func
  if not in a statement they are run using the run key word
  if not in a statement to run function in a thread import the module _thread like this: import _thread and use the thr keyword istead of the run keyword.
loops:
  there is too types of loops while and for
  while loops:
    start with the keyword while, the condition is placed before the { character and end with the }while
  conditional operators:
    equal to is ==
    not equal to is !=
    equal or greater than is >=
    equal or less than is <=
    or is simply or
    and is and
    less than is <
    greater than is >
  
  
  


