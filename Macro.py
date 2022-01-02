import tkinter as tk
import webbrowser
import subprocess

window = tk.Tk()

#Changers window name, size, makes window transparent
window.title('Web shooters')
window.geometry("400x300")
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
button_name_list = [
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

# zip lists together to form a list of tuples
zip_list = zip(button_name_list, button_label_list, button_command_list)

for name,label,cmd in zip_list:
    btn = tk.Button(window,text = label,width=15, command=cmd )
    btn.pack(pady=3)
    button_dict[name] = btn




# for y in range(3):
#     window.columnconfigure(y, weight=1, minsize=75) #
#     window.rowconfigure(y, weight=1, minsize=50)

#     for x in range(0, 3):
#         button = tk.Button(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=0,
#             padx=5,
#             pady=5

#         )

#         button.grid(row=y, column=x, )
        

        # button= tk.Button(master=frame, text=f"Row {i}\nColumn {j}")
        #button.pack(padx=5, pady=5)

window.mainloop()