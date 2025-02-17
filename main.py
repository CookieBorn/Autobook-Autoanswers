from tkinter import *
import os


from window import Window

def get_files(folder):
    files=[]
    directory=os.listdir(folder)
    for item in directory:
        if os.path.isfile(os.path.join(folder,item)):
            files.append(item)
    files=sorted(files)
    return files
def main():
    print("hello")
    files=get_files("Autobooks")
    win=Window("test",900,900,files)
    win.wait_for_close()
    print(files)

main()
