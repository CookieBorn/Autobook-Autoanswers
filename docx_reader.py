import os
import tkinter
from docx import Document
from tkinter.ttk import *
import random

class DOC_reader:
    def __init__(self, name, win, create=False, answer=False):
        self.name = name
        self.win = win
        self.location = os.path.join(self.win.folder, name)
        self.doc = Document(self.location)
        self.page=None
        self.tables=None
        self.create=create
        self.progres=None
        self.prog_var=tkinter.DoubleVar()
        self.answer=answer

        if self.create is False:
            self.progress()
            self.strip_errors()

        if self.answer is False:
            button_answer=tkinter.Button(text="Answer", background="green", command=self.solve_auto)
            self.win.canvas.create_window(200,100,window=button_answer)
            button_create=tkinter.Button(text="Create", background="green", command=self.create_auto)
            self.win.canvas.create_window(300,100,window=button_create)

        if self.answer is True:
            self.solve_auto()


    def solve_addition(self,table,k):
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                if table.cell(i,0).text != "" and table.cell(0,g).text != "":
                   table.cell(i,g).text=str(int(table.cell(0,g).text)+int(table.cell(i,0).text))
                   k=self.progress_update(k)
        return k

    def solve_subtraction(self, table,k):
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                if table.cell(i,0).text != "" and table.cell(0,g).text != "":
                    table.cell(i,g).text=str(float(table.cell(0,g).text)-float(table.cell(i,0).text))
                    k=self.progress_update(k)
        return k

    def solve_multiplication(self, table,k):
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                if table.cell(i,0).text != "" and table.cell(0,g).text != "":
                    table.cell(i,g).text=str(float(table.cell(0,g).text)*float(table.cell(i,0).text))
                    k=self.progress_update(k)
        return k

    def solve_division(self, table,k):
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                if table.cell(i,g).text != " " and table.cell(i,g).text != "":
                    table.cell(i,0).text=str(float(table.cell(i,g).text)/float(table.cell(0,g).text))
                    k=self.progress_update(k,0.5)
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                if table.cell(i,0).text != " " and table.cell(i,0).text != "":
                    table.cell(i,g).text=str(float(table.cell(0,g).text)*float(table.cell(i,0).text))
                    k=self.progress_update(k,0.5)
        return k

    def solve_auto(self):
        k=0.0
        self.progress()
        for table in self.doc.tables:
            if table.cell(0,0).text=="+":
                k=self.solve_addition(table,k)
            elif table.cell(0,0).text=="-":
                k=self.solve_subtraction(table,k)
            elif table.cell(0,0).text=="x":
                if table.cell(1,0).text != "":
                    k=self.solve_multiplication(table,k)
                else:
                    k=self.solve_division(table,k)
        self.doc.save(os.path.join(self.win.folder, self.name[:-5]+"-answers"+self.name[-5:]))
        self.win.popup_text("Answers Complete")

    def create_auto(self):
        k=0
        self.progress()
        for table in self.doc.tables:
            if table.cell(0,0).text=="+" or table.cell(0,0).text=="-" or table.cell(0,0).text=="x":
                for i in range(1, len(table.columns)):
                    table.cell(0,i).text=str(random.randint(0,10))
                    k=self.progress_update(k)
                for g in range(1,  len(table.rows)):
                    table.cell(g,0).text=str(random.randint(0,10))
                    k=self.progress_update(k)
        self.doc.save(os.path.join(self.win.folder, self.name[:-5]+"-random"+self.name[-5:]))
        self.win.popup_text("Student Copy Complete")
        self.__init__(self.name[:-5]+"-random"+self.name[-5:], self.win, answer=True)

    def strip_errors(self):
        k=0
        self.progress()
        for table in self.doc.tables:
            if table.cell(0,0).text=="+" or table.cell(0,0).text=="-" or table.cell(0,0).text=="x":
                zero_zero=table.cell(0,0).text
                for i in range(len(table.rows)):
                    for g in range(len(table.columns)):
                        table.cell(i,g).text="".join(c for c in table.cell(i,g).text if c.isdigit() or c=="-")
                        k=self.progress_update(k)
                table.cell(0,0).text=zero_zero
        self.doc.save(self.location)


    def progress(self):
        self.progres = Progressbar(self.win.canvas, orient = 'horizontal',variable=self.prog_var, maximum = (len(self.doc.tables)*110), mode = 'determinate')
        self.progres.place(x=self.win.width/4,y=400,width=self.win.width/2)

    def progress_update(self, k,x=1.0):
        self.prog_var.set(k)
        self.win.root.update_idletasks()
        k+=x
        return k
