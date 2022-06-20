from tkinter import *

class userProxy(Frame):
	def __init__(self, container):
		super().__init__(container)

		self.label = Label(self, text="I am the user proxy")
		self.label.pack()
