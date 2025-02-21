import os
from docx import Document
from window import Window


def main():
    win=Window("test",900,900,"Autobooks")
    win.wait_for_close()

main()
