import tkinter as tk

root = tk.Tk()
root.withdraw()
 

Filename = None

def newfile(): 
	global filename
	filename = "Untitled"
	text.delete(0, 0, END)

def saveFile():
	global filename
	t = text.get(0, 0 )
	f = open(filename, 'w')
	f.write(t)
	f.close()

def saveas():
	f = saveasfile(mode = 'w', defaultextension = '.txt')
	t = text.get(0.0, )
	try:
		[f.write(t.rstrip)()]
	except:
		showerror(title = "Whoopsie!!", message = "Unable to save file...")

def openFile():
	f = askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

root = Tk()
root.title("Sulai\s Python Text Editor")
root.minsize(width = 400, height = 400)
roo.maxsize(width = 400, height = 400)

text = text(root, width = 400, height = 400)
text.pack()

menubar = Menu(root)
fileMenu = Menu(menubar)
fileMenu.add_command(label = "New", command = newFile)
fileMenu.add_command(label = "Open", commnad = openFile)
fileMenu.add_command(label = "Save", command = saveFile)
fileMenu.add_command(label = "Sve As...", command = saveas)
fileMenu.add_Separator()
fileMenu.add_command(label = "Quit", command = root.Quit)
menubar.add_cascade(label = "File", menu = fileMenu)

root.mainloop()

