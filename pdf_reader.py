import os
import fitz


class PDF_reader:
    def __init__(self, name, win):
        self.name = name
        self.win = win
        self.location = os.path.join(self.win.folder, name)
        self.doc = fitz.open(self.location)
        self.print()

    def print(self):
        for page_num in range(len(self.doc)):
            page = self.doc.load_page(page_num)
            text = page.get_text()
