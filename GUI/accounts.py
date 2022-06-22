from tkinter import *
from tkinter.dnd import *
from tkinter.filedialog import askopenfilename
import tkinter.font

from commands.instabot import *
from commands.tiktokbot import *
import enum

class account(Frame):
	def __init__(self, container, accountnumber):
		super(account, self).__init__()

		def focusIn(entry):
			if entry.cget('fg') == 'grey':
				entry.delete(0, "end")
				entry.insert(0, '')
				entry.config(fg='white', bd=0, highlightthickness=4, highlightcolor='green')

		def focusOut(entry, text):
			if entry.get() == '':
				entry.insert(0, text)
				entry.config(fg='grey', highlightthickness=0, state='normal')

		# setup bots
		def startupInstagram():
			self.currentSocial = social.INSTAGRAM
			self.bots[social.INSTAGRAM].boot()
			self.bots[social.INSTAGRAM].login()
		
		def startupTitkTok():			
			self.currentSocial = social.TIKTOK
			self.bots[social.TIKTOK].boot()
			self.bots[social.TIKTOK].login()

		def submitButton():
			if self.currentSocial < 0:
				print("You haven't logged in any social!")
			elif self.filepath == "":
				print("You didn't choose any image or video!")
			else:
				self.bots[self.currentSocial].post()

		def chooseFile():
			self.filepath = askopenfilename(title='Open a File',filetypes=[("All Files", "*.*")])
			#print(self.filepath)

		# we use this class to make more easier to read which social is used
		class social():
			INSTAGRAM = 0
			TIKTOK = 1

		# Setup array that will contain our bots
		self.bots = [ InstagramBot(), TikTokBot() ]

		# this is used for the "Submit" button where we have
		# to know which social to post the image/video
		self.currentSocial = -1			

		# this will hold the image/video path for posting
		self.filepath = ""

		# Fonts
		self.normal = tkinter.font.Font(family="Poppins Regular", size=14, weight="normal")
		self.button = tkinter.font.Font(family="Poppins SemiBold", size=14, weight="normal")
		self.semibold = tkinter.font.Font(family="Poppins SemiBold", size=18, weight="normal")
		self.bold = tkinter.font.Font(family="Poppins Bold", size=26, weight="normal")

		# Title
		self.title = Label(self, text="Account " + str(accountnumber))
		self.title.grid(row=0, column=0, pady=(20, 50))
		self.title.configure(font=self.bold, bd=0)

		# form frame
		self.formFrame = LabelFrame(self, text="Insert your E-mail or Username:")
		self.formFrame.grid(row=1, column=0, sticky=W)
		self.formFrame.configure(font=self.semibold, bd=0)

		# username entry
		self.foreUsername = Entry(self.formFrame, bd=0)
		self.foreUsername.grid(row=0, column=0, ipadx=150, ipady=5, pady=5)
		self.foreUsername.configure(fg='white', bd=0, highlightthickness=4, highlightcolor='green', font=self.normal)

		self.username = Entry(self.formFrame, bd=0)
		self.username.grid(row=0, column=0, ipadx=150, ipady=5, pady=5)
		self.username.insert(0, 'E-mail/Username')
		self.username.bind('<FocusIn>', lambda event: focusIn(self.username))
		self.username.bind('<FocusOut>', lambda event: focusOut(self.username, 'E-mail'))
		self.username.bind('<Return>', lambda event: self.focus())
		self.username.configure(fg='grey', font=self.normal)

		# password entry
		self.forePassword = Entry(self.formFrame, bd=0)
		self.forePassword.grid(row=1, column=0, ipadx=150, ipady=5, pady=5)
		self.forePassword.configure(fg='white', bd=0, highlightthickness=4, highlightcolor='green', font=self.normal)

		self.password = Entry(self.formFrame, bd=0)
		self.password.grid(row=1, column=0, ipadx=150, ipady=5, pady=5)
		self.password.insert(0, "Password")
		self.password.bind('<FocusIn>', lambda event: focusIn(self.password))
		self.password.bind('<FocusOut>', lambda event: focusOut(self.password, 'Password'))
		self.password.bind('<Return>', lambda event: self.focus())
		self.password.configure(fg='grey', font=self.normal)

		# login Instagram
		self.getCredentials = Button(self.formFrame, text="Login Instagram", command=startupInstagram)
		self.getCredentials.grid(row=0, column=1, rowspan=2, padx=(100, 0), ipady=20, ipadx=10)
		self.getCredentials.configure(font=self.button)
		
		# login TikTok
		self.getCredentials = Button(self.formFrame, text="Login TikTok", command=startupTitkTok)
		self.getCredentials.grid(row=0, column=2, sticky=W, rowspan=2, ipady=20, ipadx=10)
		self.getCredentials.configure(font=self.button)

		# post frame
		self.postFrame = LabelFrame(self, text="Insert post informations:")
		self.postFrame.grid(row=2, column=0, pady=30, sticky=W)
		self.postFrame.configure(font=self.semibold, bd=0)

		# description entry
		self.foreDescription = Entry(self.postFrame, bd=0)
		self.foreDescription.grid(row=0, column=0, ipadx=150, ipady=5, pady=5)
		self.foreDescription.configure(fg='white', bd=0, highlightthickness=4, highlightcolor='green', font=self.normal)

		self.description = Entry(self.postFrame, bd=0)
		self.description.grid(row=0, column=0, ipadx=150, ipady=5, pady=5)
		self.description.configure(font=self.normal)
		self.description.insert(0, "Post description")
		self.description.bind('<FocusIn>', lambda event: focusIn(self.description))
		self.description.bind('<FocusOut>', lambda event: focusOut(self.description, 'Post description'))
		self.description.bind('<Return>', lambda event: self.focus())
		self.description.configure(fg='grey', font=self.normal)

		# hashtags entry
		self.foreHashtags = Entry(self.postFrame, bd=0)
		self.foreHashtags.grid(row=1, column=0, ipadx=150, ipady=5, pady=5)
		self.foreHashtags.configure(fg='white', bd=0, highlightthickness=4, highlightcolor='green', font=self.normal)

		self.hashtags = Entry(self.postFrame, bd=0)
		self.hashtags.grid(row=1, column=0, ipadx=150, ipady=5, pady=5)
		self.hashtags.configure(font=self.normal)
		self.hashtags.insert(1, "Post hashtags")
		self.hashtags.bind('<FocusIn>', lambda event: focusIn(self.hashtags))
		self.hashtags.bind('<FocusOut>', lambda event: focusOut(self.hashtags, 'Post hashtags'))
		self.hashtags.bind('<Return>', lambda event: self.focus())
		self.hashtags.configure(fg='grey', font=self.normal)

		# post credentials button
		self.getPostCredentials = Button(self.postFrame, text="Submit", command=submitButton)
		self.getPostCredentials.grid(row=0, column=1, rowspan=2, ipady=20, padx=(100, 0), ipadx=10)
		self.getPostCredentials.configure(font=self.button)

		# video path button
		self.getVideoPath = Button(self.postFrame, text="Select image/video path", command=chooseFile)
		self.getVideoPath.grid(row=0, column=2, rowspan=2, padx=(25, 0), ipady=20)
		self.getVideoPath.configure(font=self.button)

		# status bar
		self.statusbar = Label(self, text="Waiting", borderwidth=2, relief="solid")
		self.statusbar.grid(row=3, column=0, columnspan=2, ipadx=250, pady=20, ipady=8)
		self.statusbar.configure(font=self.normal)

		# Instagram status bar
		self.statusbar = Label(self, text="Waiting", borderwidth=2, relief="solid")
		self.statusbar.grid(row=4, column=0, columnspan=2, ipadx=250, pady=20, ipady=8)
		self.statusbar.configure(font=self.normal)