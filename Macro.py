import tkinter as tk
from tkinter.constants import BOTH
import tkinter.ttk as ttk
import webbrowser
import subprocess



window = tk.Tk()

#Changers window name, size, makes window transparent

window.title('Web shooters')
# window.geometry("300x200")
window.attributes('-alpha',0.5)


#functions for buttons

button_dict = {}

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



# each button has its own name, label and command

button_label_list = [
'Github',
'SoloLearn',
'Portfolio',
'Vscode',
'Netflix',
'Disney+',
'Apple Music',
'New tab',
'finder'
]

button_color = [
    "#FF7F50",
    "#228B22",
    "#000080",
    "#FFD700",
    "#DC143C",
    "#FF8C00",
    "#F0E68C",
    "#87CEFA",
    "#ffff00",
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
    frame1 = tk.Frame(master = window, relief = tk.RAISED, bg="#F08080", borderwidth=1)
    frame1.grid(row=1, column=1, padx=5, pady=5)

    btn = tk.Button(master =frame1,text = button_label_list[0],width=8,height=4,highlightbackground='#F08080',command=button_command_list[0])            
    btn.pack(padx=5, pady=5)
    break


##Sololearn button

window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(1, weight=1,minsize=50)

for j in range(1,2):
    frame2 = tk.Frame(master = window, relief = tk.RAISED, bg="#228B22", borderwidth=1)
    frame2.grid(row=1, column=2, padx=5, pady=5)

    btn1 = tk.Button(frame2,text = button_label_list[1],width=8,height=4,highlightbackground='#228B22',command=button_command_list[1] )            
    btn1.pack(padx=5, pady=5)
    break


###portfolio button

window.columnconfigure(3, weight=1, minsize=75)
window.rowconfigure(1, weight=1,minsize=50)

for j in range(2,3):
    frame3 = tk.Frame(master = window, relief = tk.RAISED, bg="#87CEFA", borderwidth=1)
    frame3.grid(row=1, column=3, padx=5, pady=5)

    btn2 = tk.Button(frame3,text = button_label_list[2],width=8, height=4, highlightbackground='#87CEFA',command=button_command_list[2] )   
    btn2.pack(padx=5, pady=5)   
    break 
        

#### VScode button

window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)

for j in range(0,1):
    frame4 = tk.Frame(window, relief = tk.RAISED,bg='#DC143C',borderwidth=1)
    frame4.grid(row=2, column=1, padx=5, pady=5)

    btn3 = tk.Button(frame4,text = button_label_list[3],width=8,height=4,highlightbackground='#DC143C',command=button_command_list[3] )            
    btn3.pack(padx=5, pady=5)         

##### netflix button

window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=50)

for j in range(1,2):
    frame5 = tk.Frame(window, relief = tk.RAISED,bg='#000080',borderwidth=1)
    frame5.grid(row=2, column=2, padx=5, pady=5)

    btn4 = tk.Button(frame5,text = button_label_list[4],width=8,height=4,highlightbackground='#000080',command=button_command_list[4])            
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

####### appleMusic

window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(3, weight=1, minsize=50)

for j in range(0,1):
    frame7 = tk.Frame(window, relief = tk.RAISED,bg='#FF8C00',borderwidth=1)
    frame7.grid(row=3, column=1, padx=5, pady=5)

    btn6 = tk.Button(frame7,text = button_label_list[6],width=8,height=4,highlightbackground='#FF8C00',command=button_command_list[6] )            
    btn6.pack(padx=5, pady=5)

######## newTab

window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(3, weight=1, minsize=50)

for j in range(1,2):
    frame8 = tk.Frame(window, relief = tk.RAISED,bg='#FF8C00',borderwidth=1)
    frame8.grid(row=3, column=2, padx=5, pady=5)

    btn7 = tk.Button(frame8,text = button_label_list[7],width=8, height=4,highlightbackground='#FF8C00',command=button_command_list[7] )            
    btn7.pack(padx=5, pady=5)

# ######### finder

window.columnconfigure(3, weight=1, minsize=75)
window.rowconfigure(3, weight=1, minsize=50)

for j in range(2,3):
    frame9 = tk.Frame(window, relief = tk.RAISED,bg='#FF8C00',borderwidth=1)
    frame9.grid(row=3, column=3, padx=5, pady=5)

    btn8 = tk.Button(frame9,text = button_label_list[8],width=8,height=4,highlightbackground='#FF8C00',command=button_command_list[8])            
    btn8.pack(padx=5, pady=5)


    
    window.lift()
    window.attributes('-topmost', True)
    window.grab_set()
    window.focus_force()
    window.grab_release()

window.mainloop()