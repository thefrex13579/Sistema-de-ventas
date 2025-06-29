from tkinter import Tk, Frame 
from container import Container

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Sistema de Ventas Annamar")
        self.resizable(False, False)
        self.configure(bg="#C6D9E3")
        self.geometry("800x400+120+20")

        self.container = Frame(self, bg="#C6D9E3")
        self.container.pack(fill="both", expand=True)

        self.frames = {
            Container: None
        }

        self.load_frame()
        self.show_frame(Container)

    def load_frame(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

def main():
    app = Manager()
    app.mainloop()

if __name__ =="__main__":
    main()