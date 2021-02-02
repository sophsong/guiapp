import tkinter as tk 
from tkinter import filedialog, Text
import os


root = tk.Tk() #html that holds the whole structure
#border_effect = {
    #'groove': tk.GROOVE
#}
apps = []
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = '/', title='Select File',
    filetypes=(('applications', '*.app'), ('all files', '*.*')))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, #this is where you are attaching the label to#
        text=app, bg='gray')
        label.pack()

def runApps():
    for app in apps:
        os.system(app)

canvas = tk.Canvas(root, height= 700, width=700,bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely= 0.1)

openButton = tk.Button(root, text='Open File', padx=10, pady=5, command=addApp)
openButton.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=10, command=runApps)
runApps.pack()
root.mainloop()