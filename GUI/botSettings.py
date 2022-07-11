from re import I
from tkinter import *
import tkinter.font
from turtle import width


class botSettings(Frame):
    def __init__(self, container):
        super().__init__(container)
        # Fonts
        self.normal = tkinter.font.Font(
            family="Poppins Regular", size=14, weight="normal"
        )
        self.button = tkinter.font.Font(
            family="Poppins SemiBold", size=14, weight="normal"
        )
        self.semibold = tkinter.font.Font(
            family="Poppins SemiBold", size=18, weight="normal"
        )
        self.bold = tkinter.font.Font(family="Poppins Bold", size=26, weight="normal")

        # Title Frame
        self.title_frame = Frame(self)
        self.title_frame.pack()

        # Body Frame
        self.body_frame = Frame(self)
        self.body_frame.pack(fill="x", anchor=W)

        # Title
        self.title = Label(self.title_frame, text="Bot Settings")
        self.title.configure(font=self.bold)
        self.title.grid(row=0, column=0, sticky=N)

        # Checkbox - LabelFrame
        self.auto_post_frame = LabelFrame(
            self.body_frame, text="Auto post settings", bd=0
        )
        self.auto_post_frame.configure(font=self.semibold)
        self.auto_post_frame.grid(row=0, column=0, padx=(20, 0))

        self.i = IntVar()
        self.checkbox = Checkbutton(
            self.auto_post_frame,
            text="Auto post",
            variable=self.i,
            command=lambda: print(self.i.get()),
        )
        self.checkbox.configure(font=self.normal)
        self.checkbox.grid(row=0, column=0, padx=(20, 0), pady=(15, 0))

        # Text
        self.sleeping_text = Label(self.auto_post_frame, text="The bot will sleep for")
        self.sleeping_text.configure(font=self.normal)
        self.sleeping_text.grid(row=1, column=0, padx=(40, 0), pady=(10, 0))

        # Posting delay
        self.menu_text = StringVar()
        self.menu_text.set("Hrs")
        self.menu_values = {
            "1 Hour": 1,
            "2 Hours": 2,
            "3 Hours": 3,
            "4 Hours": 4,
            "5 Hours": 5,
        }
        self.bot_sleeping_time = OptionMenu(
            self.auto_post_frame, self.menu_text, *self.menu_values
        )
        self.bot_sleeping_time.configure(font=self.normal)
        self.bot_sleeping_time.grid(row=1, column=1, pady=(10, 0))
