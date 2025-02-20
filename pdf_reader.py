import os
import fitz
from autoblock import Autoblock
from pprint import pprint
from docx import Document

class DOC_reader:
    def __init__(self, name, win):
        self.name = name
        self.win = win
        self.location = os.path.join(self.win.folder, name)
        self.doc = Document(self.location)
        self.page=None


    def Doc_text(self):
        self.doc.add_heading("Test",0)
        for p in self.doc.paragraphs:
           print(p.text)

    def print(self):
        text=""
        for page_num in range(len(self.doc)):
           self.page = self.doc[page_num]
           text += self.page.get_text()
           lines=text.split("\n")
           fil_lines=[]
           for line in lines:
               if line!=" ":
                   fil_lines.append(line)
           ind=0
           while ind<len(fil_lines):
               if fil_lines[ind]=="+ ":
                   block=Autoblock(fil_lines[ind] ,fil_lines[ind+1:(ind+21)])

               ind+=1

    def find_table(self):
        page=self.doc[3]
        tabs=page.find_tables()
        print(f"{len(tabs.tables)} found on {page}")

        if tabs.tables:
            pprint(tabs[0].extract())

    def replace_text(self,block):
        hits=self.page.search_for(block.symbol)
        for rect in hits:
            self.page.add_redact_annot(rect,block.answers,fontname="helv",fontsize=11,align=fitz.TEXT_ALIGN_CENTER)
        self.page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
        self.doc.save(self.name,garbage=3,deflate=True)
