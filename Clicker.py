from tkinter import *


class Clicker(Frame):
    def __init__(self, master):
        super(Clicker, self).__init__(master)
        self.grid()
        self.clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.text = Label(self, text="Number of clicks: 0")
        self.text.grid(row=0, column=0, columnspan=2, sticky=W)

        self.button = Button(text="Click here", command=self.counter)
        self.button.grid()

    def counter(self):
        self.clicks += 1
        self.text["text"] = "Number of cliks: " + str(self.clicks)


if __name__ == "__main__":
    root = Tk()
    root.title("Click for achievements!")
    root.geometry("300x50")
    Clicker(root)
    root.mainloop()
