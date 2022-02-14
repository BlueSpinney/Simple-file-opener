from tkinter import *
import cv2 as cv
import os
import sys 

counter = 0

main = Tk()

enter = Entry(main,bd=1.5)

name = ""
path = ""
exe = ""


def safe_read():
    global counter
    global name
    global path
    global exe
    
    name = enter.get()
    
    counter = counter + 1
    
    with open('safe.txt','a') as safe_file:
        safe_file.write( str(counter) + " s/ " + name + " \e")
    
    if counter == 6:
        counter = 0
        with open('safe.txt','w') as safe_file:
            safe_file.write("")
    
    b2.configure(text=name)
    
    if name.find("!filepath") > 0:
        path = name[name.find("!filepath")+ 10:name.find("!name")]
    if name.find("!name") > 0:
        exe = name[name.find("!name")+6:1000]
        
    b2.pack()
            
def open_file():
    global name
    global path
    global exe
    print('cmd /k "D: && cd "'+ path + ' " && "' + exe + '".exe && exit"')
    os.system('cmd /k "D: && cd "'+ path + ' " && "' + exe + '".exe && exit"')

    
    

header = Label(main,text="game quick axis")

b1 = Button(main,text="safe",command=safe_read)

b2 = Button(main,text="",command=open_file)


header.pack()
b1.pack()
b2.pack()
enter.pack()
main.mainloop()