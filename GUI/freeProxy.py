from tkinter import *

class freeProxy(Frame):
	def __init__(self, container):
		super().__init__(container)

		self.label = Label(self, text="I am the free proxy")
		self.label.pack()
