from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename
import os


class notepad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("550x400")
        self.maxsize(width=550, height=400)
        self.minsize(width=250, height=280)
        self.title("untitled - notepad")
        self.config(bg="white")
        self.txt = Text(self, font="lucida 10")
        self.txt.pack(expand=True, fill=BOTH)
        self.file = None
        self.menubar()

    def newfile(self):
        self.title("untitled")
        self.file = None
        self.txt.delete(1.0, END)

    def openfile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[
                                    ("all Files", "*.*"), ("Text Document", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.txt.delete(1.0,END)
            self.title(os.path.basename(self.file))
        with open(self.file, "r") as f:
            f = f.read()
            self.txt.insert(1.0, f)

    def savefile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile='untitled.txt', defaultextension=".txt", filetypes=[
                                          ("all Files", "*.*"), ("Text Document", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                with open(self.file, "w") as f:
                    f.write(self.txt.get(1.0, END))
                self.title(os.path.basename(self.file))

    def menubar(self):
        self.menu_b = Menu(self)
        self.filemenu = Menu(self.menu_b, tearoff=0)
        self.filemenu.add_command(label="New file", command=self.newfile)
        self.filemenu.add_command(label="open file", command=self.openfile)
        self.filemenu.add_command(label="Save as", command=self.savefile)
        self.filemenu.add_separator()
        self.menu_b.add_cascade(label="File", menu=self.filemenu)
        self.config(menu=self.menu_b)


note = notepad()
note.mainloop()
