from tkinter import *

class dashboard(Frame):
	def __init__(self, container):
		super().__init__(container)

		self.label = Label(self, text="I am the dashboard")
		self.label.pack()
