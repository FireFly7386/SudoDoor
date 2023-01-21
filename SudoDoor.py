import tkinter as tk
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

#Initiating Window
root = tk.Tk()
root.title("SudoDoor v0.1 Beta")

try:
    root.state('zoomed')
except:
    root.attributes('-zoomed',True)

#Toggle Fullscreen
root.bind('<Control-Shift-KeyPress-F>', toggleFullscreen)

root.mainloop()