import os
from docx import Document
from window import Window


def main():
    document = Document(os.path.join('Autobooks','test.docx'))
    document.add_heading('Heading for the document 2', 2)
    document.save(os.path.join('Autobooks','test.docx'))
    win=Window("test",900,900,"Autobooks")
    win.wait_for_close()
    print(win.files)

main()
