from tkinter import *

from Clicker import Clicker


class TestClicker:
    def create_the_frame():
        root = Tk()
        root.title("Click for achievements!")
        root.geometry("300x50")
        return root

    def test_initialisation(self):
        clicker = Clicker
        assert clicker

    def test_initial_counter(self):
        root = TestClicker.create_the_frame()
        clicker = Clicker(root)
        root.after(1000, lambda: root.destroy())
        root.mainloop()
        assert clicker.clicks == 0

    def test_first_click_counting(self):
        root = TestClicker.create_the_frame()
        clicker = Clicker(root)
        clicker.button.invoke()
        root.after(1000, lambda: root.destroy())
        root.mainloop()
        assert clicker.clicks == 1

    def test_several_clicks_counting(self):
        root = TestClicker.create_the_frame()
        clicker = Clicker(root)
        for i in range(5):
            clicker.button.invoke()
            i += 1
        root.after(1000, lambda: root.destroy())
        root.mainloop()
        assert clicker.clicks == 5
