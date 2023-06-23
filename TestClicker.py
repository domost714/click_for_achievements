from tkinter import *

from Clicker import Clicker


class TestClicker:
    def verify_button_after_clicking(times):
        root = Tk()
        root.title("Click for achievements!")
        root.geometry("250x75")
        clicker = Clicker(root)
        for i in range(times):
            clicker.button.invoke()
            i += 1
        if times < 10:
            assert str(bool(clicker.achievements.grid_info())) == "False"
        else:
            assert str(bool(clicker.achievements.grid_info())) == "True"
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

    def test_achievements_label_unlocking(self):
        TestClicker.verify_button_after_clicking(10)