import os
from docx import Document
from tkinter import *
import random

class DOC_reader:
    def __init__(self, name, win, create=False):
        self.name = name
        self.win = win
        self.location = os.path.join(self.win.folder, name)
        self.doc = Document(self.location)
        self.page=None
        self.tables=None
        self.create=create

        if self.create is False:
            self.strip_errors()


        button_answer=Button(text="Answer", background="green", command=self.solve_auto)
        self.win.canvas.create_window(200,100,window=button_answer)

        button_create=Button(text="Create", background="green", command=self.create_auto)
        self.win.canvas.create_window(300,100,window=button_create)





    def Doc_text(self):
        self.doc.add_heading("Test",0)
        for p in self.doc.paragraphs:
           print(p.text)

    def solve_addition(self,table):
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                table.cell(i,g).text=str(int(table.cell(0,g).text)+int(table.cell(i,0).text))

    def solve_subtraction(self, table):
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                table.cell(i,g).text=str(float(table.cell(0,g).text)-float(table.cell(i,0).text))

    def solve_multiplication(self, table):
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                table.cell(i,g).text=str(float(table.cell(0,g).text)*float(table.cell(i,0).text))

    def solve_division(self, table):
        for i in range(1, len(table.rows)):
            for g in range(1, len(table.columns)):
                if table.cell(i,g).text != " " and table.cell(i,g).text != "":
                    table.cell(i,0).text=str(float(table.cell(i,g).text)/float(table.cell(0,g).text))
            for i in range(1, len(table.rows)):
                for g in range(1, len(table.columns)):
                    if table.cell(i,0).text != " " and table.cell(i,0).text != "":
                        table.cell(i,g).text=str(float(table.cell(0,g).text)*float(table.cell(i,0).text))

    def solve_auto(self):
        for table in self.doc.tables:
            if table.cell(0,0).text=="+":
                self.solve_addition(table)
            elif table.cell(0,0).text=="-":
                self.solve_subtraction(table)
            elif table.cell(0,0).text=="x":
                if table.cell(1,0).text != "":
                    self.solve_multiplication(table)
                else:
                    self.solve_division(table)
        self.doc.save(self.location)

    def create_auto(self):
        for table in self.doc.tables:
            if table.cell(0,0).text=="+" or table.cell(0,0).text=="-" or table.cell(0,0).text=="x":
                for i in range(1, len(table.columns)):
                    table.cell(0,i).text=str(random.randint(0,10))
                for g in range(1,  len(table.rows)):
                    table.cell(g,0).text=str(random.randint(0,10))
        self.doc.save(os.path.join(self.win.folder, self.name[:-5]+"-random"+self.name[-5:]))

    def strip_errors(self):
        for table in self.doc.tables:
            if table.cell(0,0).text=="+" or table.cell(0,0).text=="-" or table.cell(0,0).text=="x":
                zero_zero=table.cell(0,0).text
                for i in range(len(table.rows)):
                    for g in range(len(table.columns)):
                        table.cell(i,g).text="".join(c for c in table.cell(i,g).text if c.isdigit() or c=="-")
                table.cell(0,0).text=zero_zero
        self.doc.save(self.location)
