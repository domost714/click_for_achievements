from tkinter import *


class Clicker(Frame):
    def __init__(self, master):
        super(Clicker, self).__init__(master)
        self.grid()
        self.clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.text = Label(self, text="Number of clicks: 0")
        self.text.grid(column=0, row=0, sticky=W, padx=5, pady=5)

        self.button = Button(text="Click here", command=self.counter)
        self.button.grid(column=0, row=1, sticky=W, padx=5, pady=5)

        self.achievements = Label(self, text="Achievements:")
        self.achievements.grid(column=1, row=0, sticky=E, padx=5, pady=5)

    def counter(self):
        self.clicks += 1
        self.text["text"] = "Number of cliks: " + str(self.clicks)


if __name__ == "__main__":
    root = Tk()
    root.title("Click for achievements!")
    root.geometry("250x75")
    Clicker(root)
    root.mainloop()
