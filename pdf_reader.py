import os
import fitz
from autoblock import Autoblock


class PDF_reader:
    def __init__(self, name, win):
        self.name = name
        self.win = win
        self.location = os.path.join(self.win.folder, name)
        self.doc = fitz.open(self.location)
        self.print()

    def print(self):
        text=""
        for page_num in range(len(self.doc)):
           page = self.doc.load_page(page_num)
           text += page.get_text()
        lines=text.split("\n")
        fil_lines=[]
        for line in lines:
            if line!=" ":
                fil_lines.append(line)
        ind=0
        while ind<len(fil_lines):
            if fil_lines[ind]=="+ ":
                Autoblock(fil_lines[ind] ,fil_lines[ind+1:(ind+21)])
            ind+=1
