from tkinter import *
import shutil
import os
from docx_reader import DOC_reader
from pdf_reader import PDF_reader

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
        self.clicked=StringVar()
        self.file_menu=None
        self.get_files()
        self.clicked.set(self.files[0])
        self.file_menu_select.set(self.files[0])

        button_create=Button(text="Create", background="green", command=self.create)
        self.canvas.create_window(self.width/3,100,window=button_create)

        button_answer=Button(text="Answer", background="green", command=self.answer)
        self.canvas.create_window((self.width/3)*2,100,window=button_answer)

    def answer(self):
        self.popup_screen("Answer")

        button_copy=Button(text="Copy", background="green", command=self.copy)
        self.canvas.create_window(200,300,window=button_copy)

        button_load=Button(text="Load", background="green", command=self.load)
        self.canvas.create_window(300,300,window=button_load)

        self.menu()

    def create(self):
        self.popup_screen("Create")

        DOC_reader("Auto Books Template.docx", self, True)


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def file_set(self,selection):
        self.file_menu_select=selection

    def menu(self):
        if self.file_menu!=None:
            self.file_menu=None
        self.file_menu = OptionMenu(self.root,self.clicked, *self.files,command=self.file_set)
        self.canvas.create_window(600,300,window=self.file_menu)

    def copy(self):
        if str(self.file_menu_select)[-5:]==".docx":
            file_copy=str(self.file_menu_select)[:-5]+"-copy."+str(self.file_menu_select)[-4:]
        else:
            file_copy=str(self.file_menu_select)[:-4]+"-copy."+str(self.file_menu_select)[-3:]
        if os.path.isfile(os.path.join(self.folder,file_copy)):
            self.popup_text("Copy Already Created")
        else:
            self.popup_text("Copy Made")
            shutil.copyfile(os.path.join(self.folder,str(self.file_menu_select)),os.path.join(self.folder,file_copy))
            self.get_files()
            self.menu()

    def wait_for_close(self):
        self.running=True
        while self.running is True:
            self.redraw()


    def popup_text(self,text):
        self.canvas.create_rectangle(100, (self.height/6)*4, (self.width)-100, (self.height/6)*5, fill="white")
        self.canvas.create_text(self.width/2,(self.height/12)*9, text=text, fill="green", font=('Helvetica 15 bold'))

    def popup_screen(self,text):
        self.canvas.create_rectangle(100,200, (self.width)-100, (self.height)-200, fill="white")
        self.canvas.create_text(self.width/2,self.height/4, text=text, fill="green", font=('Helvetica 15 bold'))

    def close(self):
        self.running=False

    def get_files(self):
        self.files=[]
        directory=os.listdir(self.folder)
        for item in directory:
            if os.path.isfile(os.path.join(self.folder,item)):
                self.files.append(item)
        self.files=sorted(self.files)

    def load(self):
        if str(self.file_menu_select)[-4:]=="docx":
            DOC_reader(self.file_menu_select, self)
            self.popup_text(f"{self.file_menu_select} succesfully loaded")
        elif str(self.file_menu_select)[-3:]=="pdf":
            PDF_reader(self.file_menu_select, self)
            self.popup_text(f"{self.file_menu_select} succesfully loaded")
        else:
            self.popup_text("Please load a pdf or docx")
