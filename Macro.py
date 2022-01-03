import tkinter as tk
from tkinter.constants import BOTH
import tkinter.ttk as ttk
import webbrowser
import subprocess
from webbrowser import *


lastClickX = 0
lastClickY = 0

window = tk.Tk()

window.configure(bg='#696969')



# Allow window to be dragged on top level

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))

# Functions for button commands

def github():
    subprocess.run(["/usr/bin/open", "-a", "GitHub Desktop"])

def soloLearn():
    browser = webbrowser.get('Chrome')
    browser.open('https://www.sololearn.com/profile/11174869')

def portfolio():
    browser = webbrowser.get('Chrome')
    browser.open('http://127.0.0.1:5500/html5up-massively/index.html')

def vsCode():
    subprocess.run(["/usr/bin/open", "-a", "Visual Studio Code"])

def netflix():
    browser = webbrowser.get('Chrome')
    browser.open('https://www.netflix.com/browse')

def disney():
    browser = webbrowser.get('Chrome')
    browser.open('https://www.disneyplus.com/home')

def disney():
    browser = webbrowser.get('Chrome')
    browser.open('https://www.disneyplus.com/home')

def appleMusic():
    subprocess.run(["/usr/bin/open", "-a", "Music"])

def newTab():
    browser = webbrowser.get('Chrome')
    browser.open('https://www.google.com/')

def finder():
    subprocess.run(["/usr/bin/open", "-a", "finder"])

# each button has its own label and command

button_dict = {}

button_label_list = [
    'Github',
    'SoloLearn',
    'Portfolio',
    'Vscode',
    'Netflix',
    'Disney+',
    'Music',
    'New tab',
    'finder'
]

button_command_list = [
    github,
    soloLearn,
    portfolio,
    vsCode,
    netflix,
    disney,
    appleMusic,
    newTab,
    finder
]

#github button

window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(1, weight=1,minsize=50)

for j in range(0,1):
    frame1 = tk.Frame(master = window, relief = tk.SUNKEN, bg="#87CEEB", borderwidth=-2)
    frame1.grid(row=1, column=1, padx=5, pady=5)

    btn = tk.Button(master =frame1,text = button_label_list[0],width=8,height=4,highlightbackground='#1E90FF',borderwidth=-2,command=button_command_list[0])            
    btn.pack(padx=5, pady=5)
    break


##Sololearn button

window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(1, weight=1,minsize=50)

for j in range(1,2):
    frame2 = tk.Frame(master = window, relief = tk.SUNKEN, bg="#4169E1", borderwidth=-2)
    frame2.grid(row=1, column=2, padx=5, pady=5)

    btn1 = tk.Button(frame2,text = button_label_list[1],width=8,height=4,highlightbackground='#0000CD',command=button_command_list[1] )            
    btn1.pack(padx=5, pady=5)
    break


###portfolio button

window.columnconfigure(3, weight=1, minsize=75)
window.rowconfigure(1, weight=1,minsize=50)

for j in range(2,3):
    frame3 = tk.Frame(master = window, relief = tk.RAISED, bg="#3CB371", borderwidth=-2)
    frame3.grid(row=1, column=3, padx=5, pady=5)

    btn2 = tk.Button(frame3,text = button_label_list[2],width=8, height=4,borderwidth=-2 ,highlightbackground='#2E8B57',command=button_command_list[2] )   
    btn2.pack(padx=5, pady=5)   
    break 
        

#### VScode button

window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)

for j in range(0,1):
    frame4 = tk.Frame(window, relief = tk.RAISED,bg='#B0C4DE',borderwidth=1)
    frame4.grid(row=2, column=1, padx=5, pady=5)

    btn3 = tk.Button(frame4,text = button_label_list[3],width=8,height=4,highlightbackground='#4682B4',command=button_command_list[3] )            
    btn3.pack(padx=5, pady=5)         

##### netflix button

window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)

for j in range(1,2):
    frame5 = tk.Frame(window, relief = tk.RAISED,bg='#008000',borderwidth=-2)
    frame5.grid(row=2, column=2, padx=5, pady=5)

    btn4 = tk.Button(frame5,text = button_label_list[4],width=8,height=4,highlightbackground='#006400',borderwidth=-2,command=button_command_list[4])            
    btn4.pack(padx=5, pady=5)

###### disney button

window.columnconfigure(3, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)

for j in range(2,3):
    frame6 = tk.Frame(window, relief = tk.RAISED,bg='#F0E68C',borderwidth=1)
    frame6.grid(row=2, column=3, padx=5, pady=5)

    btn5 = tk.Button(frame6,text = button_label_list[5],width=8,height=4,highlightbackground='#F0E68C',command=button_command_list[5] ) 
    btn5.pack(padx=5, pady=5)
    break

####### appleMusic button

window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(3, weight=1, minsize=50)

for j in range(0,1):
    frame7 = tk.Frame(window, relief = tk.RAISED,bg='#6B8E23',borderwidth=-2)
    frame7.grid(row=3, column=1, padx=5, pady=5)

    btn6 = tk.Button(frame7,text = button_label_list[6],width=8,height=4,highlightbackground='#556B2F',borderwidth=-2,command=button_command_list[6] )            
    btn6.pack(padx=5, pady=5)

######## newTab button

window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(3, weight=1, minsize=50)

for j in range(1,2):
    frame8 = tk.Frame(window, relief = tk.RAISED,bg='#F5DEB3',borderwidth=-2)
    frame8.grid(row=3, column=2, padx=5, pady=5)

    btn7 = tk.Button(frame8,text = button_label_list[7],width=8, height=4,highlightbackground='#FFDEAD',command=button_command_list[7] )            
    btn7.pack(padx=5, pady=5)

########## finder button

window.columnconfigure(3, weight=1, minsize=75)
window.rowconfigure(3, weight=1, minsize=50)

for j in range(2,3):
    frame9 = tk.Frame(window, relief = tk.RAISED,bg='#F4A460',borderwidth=-2)
    frame9.grid(row=3, column=3, padx=5, pady=5)

    btn8 = tk.Button(frame9,text = button_label_list[8],width=8,height=4,highlightbackground='#FF8C00',command=button_command_list[8])            
    btn8.pack(padx=5, pady=5)


# Allow window to be dragged on top level
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)

# Changers window tittle, size, makes window transparent
window.title('Web shooters')
window.attributes('-alpha',0.5)

# Moves window to the topmost
window.lift(window)
window.attributes('-topmost', True)



window.mainloop()