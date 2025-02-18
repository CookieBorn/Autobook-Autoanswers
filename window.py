from tkinter.tix import ComboBox
from tkinter import *
import shutil
import os

class Window:
    def __init__(self,name, width, height, folder, run=None):
        self.height=height
        self.width=width
        self.run=run
        self.root=Tk()
        self.root.title(name)
        self.canvas=Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running=False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.file_menu_select=StringVar()
        self.folder=folder
        self.files=[]
        self.get_files()

        button_load=Button(text="Load", background="green", command=self.load)
        self.canvas.create_window(100,100,window=button_load)

        button_answers=Button(text="Answers", background="green")
        self.canvas.create_window(100,200,window=button_answers)

        option_1=self.files[0]

        self.file_menu_select=self.files[0]

        file_menu = OptionMenu(self.root,self.file_menu_select, *self.files)
        self.canvas.create_window(100,300,window=file_menu)


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def load(self):
        file_copy=str(self.file_menu_select)[:-4]+"-copy.pdf"
        if os.path.isfile(os.path.join(self.folder,file_copy)):
            self.canvas.create_oval((self.width/8)*3+100,(self.height/8)*3, (self.width/8)*5+100, (self.height/8)*5, fill="white")
            self.canvas.create_text(self.width/2+100,self.height/2, text="Copy Exists", fill="green", font=('Helvetica 15 bold'))
        else:
            self.canvas.create_oval((self.width/8)*3+100,(self.height/8)*3, (self.width/8)*5+100, (self.height/8)*5, fill="white")
            self.canvas.create_text(self.width/2+100,self.height/2, text="Copy Made", fill="green", font=('Helvetica 15 bold'))
            shutil.copyfile(os.path.join(self.folder,self.file_menu_select),os.path.join(self.folder,file_copy))

    def wait_for_close(self):
        self.running=True
        while self.running is True:
            self.redraw()

    def close(self):
        self.running=False

    def get_files(self):
        self.files=[]
        directory=os.listdir(self.folder)
        for item in directory:
            if os.path.isfile(os.path.join(self.folder,item)):
                self.files.append(item)
        self.files=sorted(self.files)
