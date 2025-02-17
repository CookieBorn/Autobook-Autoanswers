from tkinter import *

class Window:
    def __init__(self,name, width, height, run=None):
        self.height=height
        self.width=width
        self.run=run
        self.root=Tk()
        self.root.title(name)
        self.canvas=Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running=False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        button_load=Button(text="Load", background="green")
        self.canvas.create_window(self.height-100,self.width-200,window=button_load)


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running=True
        while self.running is True:
            self.redraw()

    def close(self):
        self.running=False
