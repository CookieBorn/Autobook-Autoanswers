import os
from docx import Document
from window import Window


def main():
    win=Window("Autobook Maker",900,900,"Autobooks")
    win.wait_for_close()

main()
