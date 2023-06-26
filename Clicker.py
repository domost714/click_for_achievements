from tkinter import *


class Clicker(Frame):
    def __init__(self, master):
        super(Clicker, self).__init__(master)
        self.grid()
        self.clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.text = Label(self, text="Number of clicks: 0")
        self.text.grid(column=0, row=0, sticky=W)

        self.button = Button(text="Click here", command=self.counter)
        self.button.grid(column=0, row=1, sticky=W)

        self.achievements = Label(self, text="Achievements:")

    def counter(self):
        self.clicks += 1
        self.text["text"] = "Number of cliks: " + str(self.clicks)
        if self.clicks >= 10:
            self.achievements.grid(column=1, row=0, sticky=E)


if __name__ == "__main__":
    root = Tk()
    root.title("Click for achievements!")
    root.geometry("250x75")
    Clicker(root)
    root.mainloop()
