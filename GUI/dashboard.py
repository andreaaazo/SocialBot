from tkinter import *
import tkinter.font


class dashboard(Frame):
	def __init__(self, container):
		super().__init__(container)

		# Adding fonts
		self.normal = tkinter.font.Font(family="Poppins Regular", size=14, weight="normal")
		self.semibold = tkinter.font.Font(family="Poppins SemiBold", size=16, weight="normal")
		self.bold = tkinter.font.Font(family="Poppins Bold", size=20, weight="normal")
		self.title = tkinter.font.Font(family="Poppins Bold", size=26, weight="normal")

		# Title
		self.dashboard_title = Label(self, text="Dashboard")
		self.dashboard_title.configure(font=self.title)
		self.dashboard_title.grid(row=0, column=0, pady=(20, 0), sticky = W)

		# Account 1 - Label Frame
		self.account1_frame = LabelFrame(self, bd=0, text="Account 1")
		self.account1_frame.configure(font=self.bold)
		self.account1_frame.grid(row=1, column=0, pady=(50, 0), sticky=W)

		# Account 1 - Active informations
		self.account1_active_informations_frame = LabelFrame(self.account1_frame, text="Active informations:")
		self.account1_active_informations_frame.configure(font=self.semibold)
		self.account1_active_informations_frame.grid(row=0, column=0, pady=(10, 0), sticky=W)

		self.account1_active_informations = Label(self.account1_active_informations_frame, text='email@gmail.com, "caption", #post #trap')
		self.account1_active_informations.configure(font=self.normal)
		self.account1_active_informations.grid(row=1, column=0, pady=(10, 0), sticky=W, ipady=10)

		# Account 1 - Bot status
		self.account1_bot_status_frame = LabelFrame(self.account1_frame, text="Bot status:")
		self.account1_bot_status_frame.configure(font = self.semibold)
		self.account1_bot_status_frame.grid(row=0, column=1, pady=(10, 0), stick=W, padx=(25, 0))

		self.accoun1_bot_status = Label(self.account1_bot_status_frame, text="Waiting", background='grey')
		self.accoun1_bot_status.configure(font=self.normal)
		self.accoun1_bot_status.grid(row=1, column=1, pady=(10, 0), sticky=W, ipady=5, ipadx = 150)

		# Account 1 - Short buttons
		self.account1_buttons_frame = LabelFrame(self.account1_frame, text="Buttons:")
		self.account1_buttons_frame.configure(font=self.semibold)
		self.account1_buttons_frame.grid(row=0, column=2, pady=(10, 0), sticky=W, padx=(25, 0))

		self.account1_start_button = Button(self.account1_buttons_frame, text="Start bot")
		self.account1_start_button.configure(font=self.normal)
		self.account1_start_button.grid(row=0, column=0, pady=(10, 0), sticky=W, ipady=10)