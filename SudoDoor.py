import tkinter as tk
from tkinter import *
import subprocess
import threading
import listener

def toggleFullscreen(e):
    global toggled
    global root

    if toggled == False:
        root.attributes('-fullscreen',True)
        toggled = True
    elif toggled == True:
        root.attributes('-fullscreen',False)
        toggled = False

toggled = False



def startListener(port):
    global revShellOut

    p = subprocess.Popen(listener.listen("0.0.0.0", 9001))
    while p.poll == None:
        output, errors = p.communicate()
        revShellOut.insert(END, output)
        

#Initiating Window
root = tk.Tk()
root.title("SudoDoor v0.1 Beta")

try:
    root.state('zoomed')
except:
    root.attributes('-zoomed',True)

#Toggle Fullscreen
root.bind('<Control-Shift-KeyPress-F>', toggleFullscreen)

#Make background color dark
root.configure(bg="#272727")

#Menu Bar
menubar = Menu(root)
root.configure(menu=menubar)

listener_menu = Menu(menubar)

listener_menu.add_command(
    label ='Start Listener',
    command = lambda: startListener(9001)
)

menubar.add_cascade(
    label="Listener",
    menu=listener_menu,
    underline=0
)

revShellOut = Text(root)
revShellOut.pack()

root.mainloop()