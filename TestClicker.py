from tkinter import *

from Clicker import Clicker


class TestClicker:
    def verify_button_after_clicking(times):
        root = Tk()
        root.title("Click for achievements!")
        root.geometry("300x50")
        clicker = Clicker(root)
        for i in range(times):
            clicker.button.invoke()
            i += 1
        root.after(1000, lambda: root.destroy())
        root.mainloop()
        assert clicker.clicks == times

    def test_initialisation(self):
        clicker = Clicker
        assert clicker

    def test_initial_counter(self):
        TestClicker.verify_button_after_clicking(0)

    def test_first_click_counting(self):
        TestClicker.verify_button_after_clicking(1)

    def test_several_clicks_counting(self):
        TestClicker.verify_button_after_clicking(5)
