import os
import tkinter as tk

def kill_startmenu_processes():
	os.system("taskkill /F /im SearchApp.exe")
	os.system("taskkill /F /im SearchIndexer.exe")
	os.system("taskkill /F /im StartMenuExperienceHost.exe")

root= tk.Tk()
root.title("Win10 Start Menu Process Killer")
root.iconbitmap("SpecialAttackPSO.ico") 


canvas1 = tk.Canvas(root, width = 350, height = 200)
canvas1.pack()

def killem ():  
    label1 = tk.Label(root, text= 'Attempting to kill start menu processes:\nSearchApp.exe\nSearchIndexer.exe\nStartMenuExperienceHost.exe', fg='black', font=('helvetica', 12, 'bold'))
    canvas1.create_window(175, 125, window=label1)
    kill_startmenu_processes()
    
button1 = tk.Button(text='Kill Windows 10 start menu processes',command=killem, bg='brown',fg='white')
canvas1.create_window(175, 50, window=button1)

root.mainloop()