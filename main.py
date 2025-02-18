from tkinter import *
import os


from window import Window


def main():
    win=Window("test",900,900,"Autobooks")
    win.wait_for_close()
    print(win.files)

main()
