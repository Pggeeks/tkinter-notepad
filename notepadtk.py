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
        self.file = None
        self.sbar = Scrollbar(self)
        self.sbar.pack(side=RIGHT, fill=Y)
        self.txt = Text(self, font="lucida 10")
        self.txt.pack(expand=True, fill=BOTH)
        self.txt.config(yscrollcommand=self.sbar.set)
        self.sbar.config(command=self.txt.yview)
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
            self.txt.delete(1.0, END)
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
        self.menu_b.add_command(label="Word Wrap",command=self.launch)
        self.config(menu=self.menu_b)
        #######################
    def launch(self):
        root=Tk()
        root.title("word wrap")
        root.geometry("400x320")
        root.maxsize(width=300,height=400)
        root.config(bg="white")
        self.f1=Frame(root,bg="white",bd=5,width=160,height=200,cursor="target",relief=RIDGE)
        ### buttons for font selection
        self.btn1=Button(self.f1,bg="white",fg="black",text="ABCDE abcd")
        self.btn2=Button(self.f1,bg="white",fg="black",text="ABCDE abcd")
        self.btn3=Button(self.f1,bg="white",fg="black",text="ABCDE abcd")
        self.btn4=Button(self.f1,bg="white",fg="black",text="ABCDE abcd")
        self.btn5=Button(self.f1,bg="white",fg="black",text="ABCDE abcd")
        self.btn1.place(x=27,y=8)
        self.btn2.place(x=27,y=41)
        self.btn3.place(x=27,y=74)
        self.btn4.place(x=27,y=107)
        self.btn5.place(x=27,y=140)
        Label(root,text="select font",bg="white",fg="black",font="roman 13 bold").place(x=28,y=8)
        self.f1.place(x=20,y=33)
        root.mainloop()




note = notepad()
# f_edit= FontEditMenu()
# f_edit.menubarf()
# f_edit.mainloop()
note.mainloop()
