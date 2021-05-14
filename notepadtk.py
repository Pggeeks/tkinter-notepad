from tkinter import *
class notepad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("320x350")
        self.maxsize(width=250,height=300)
        self.minsize(width=250,height=280)
        self.title("untitled - notepad")
        self.config(bg="white")
        self.txt=Text(self)
        self.txt.pack()
        self.file=None
        self.menubar()
    def newfile(self):
        pass
    def openfile(self):
        pass
    def savefile(self):
        pass
    def menubar(self):
        self.menu_b=Menu(self)
        self.filemenu=(self.menu_b)
        self.filemenu.add_command(label="New file",command=self.newfile)
        self.filemenu.add_command(label="open file",command=self.openfile)
        self.filemenu.add_command(label="Save as",command=self.savefile)
        self.filemenu.add_separator()
        self.menu_b.add_cascade(label="File",menu=self.filemenu)
        self.config(menu=self.menu_b)
note=notepad()
note.mainloop()
