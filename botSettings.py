from tkinter import *

class botSettings(Frame):
	def __init__(self, container):
		super().__init__(container)

		self.label = Label(self, text="I am the bot settings")
		self.label.pack()
