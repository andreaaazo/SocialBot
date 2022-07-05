from tkinter import StringVar

statusbar_dict = dict()


class StatusBar(StringVar):
    def __init__(self):
        super().__init__()
        self.set("Let's break the rules!")

    def change_text(self, text):
        self.set(text)
