
# fileopener

from tkinter import *
import os
import sys 

counter = 0

main = Tk()

enter = Entry(main,bd=1.5)

name = ""
path = ""
exe = ""
setuprun = False

def setup():
    global setuprun
    global name
    print("hello")
    
    with open('safe.txt', 'r') as safe_file:
        name = safe_file.read()
        print(name)
        name = name[name.find("s/") + 2:name.find("/e")]
        
    with open('safe.txt', 'w') as safe_file:
        safe_file.write("")
    
    print(name)                                                                                                                                                                                                                                                                     
    
    
    setuprun = True
    
    safe_read()
    
    
    

def safe_read():
    global counter
    global name
    global path
    global exe
    global setuprun
    
    if setuprun == False:
        name = enter.get()
    setuprun = False
    
    counter = counter + 1
    
    print(name)
    
    with open('safe.txt','w') as safe_file:
        safe_file.write( str(counter) + " s/" + name + "/e")
    
    if counter == 6:
        counter = 0
        with open('safe.txt','w') as safe_file:
            safe_file.write("")
    
    b2.configure(text=name[name.find("s/") + 1:name.find("!filepath") - 1])
    
    if name.find("!filepath") > 0:
        path = name[name.find("!filepath")+ 10:name.find("!name")]
    if name.find("!name") > 0:
        exe = name[name.find("!name")+6:1000]
        
    b2.pack()
            
def open_file():
    global name
    global path
    global exe
    print('cmd /k "D: && cd "'+ path +  " && " + exe + ".exe && exit")
    os.system('cmd /k "D: && cd "'+ path +  '" && "' + exe + '".exe && exit"')

    


header = Label(main,text="quick axis")

b2 = Button(main,text="",command=open_file)

b3 = Button(main,text="setup",command=setup)

b1 = Button(main,text="safe",command=safe_read)


Instructiontxt = Label(main,text="name (name of button) \n !filepath (path to file)  \n !name (name of application)")



header.pack()
Instructiontxt.pack()
b3.pack()
b1.pack()
b2.pack()
enter.pack()
main.mainloop()