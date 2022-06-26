from re import I
from tkinter import *
import tkinter.font

from commands.database import Database


class dashboard(Frame):
    def __init__(self, container):
        super().__init__(container)

        # Adding fonts
        self.normal = tkinter.font.Font(
            family="Poppins Regular", size=14, weight="normal"
        )
        self.semibold = tkinter.font.Font(
            family="Poppins SemiBold", size=16, weight="normal"
        )
        self.bold = tkinter.font.Font(family="Poppins Bold", size=20, weight="normal")
        self.title = tkinter.font.Font(family="Poppins Bold", size=26, weight="normal")

        # Title
        self.dashboard_title = Label(self, text="Dashboard")
        self.dashboard_title.configure(font=self.title)
        self.dashboard_title.grid(row=0, column=0, pady=(20, 0), sticky=N)

        # Database
        database = Database()

        class Accounts(LabelFrame):  # Creating accounts
            def __init__(self, container, active_informations):
                super().__init__(container)

                class Account(LabelFrame):  # Creates single account
                    def __init__(self, container, account_num, row):
                        super().__init__(container)
                        # Adding fonts
                        self.normal = tkinter.font.Font(
                            family="Poppins Regular", size=14, weight="normal"
                        )
                        self.semibold = tkinter.font.Font(
                            family="Poppins SemiBold", size=16, weight="normal"
                        )
                        self.bold = tkinter.font.Font(
                            family="Poppins Bold", size=20, weight="normal"
                        )
                        self.title = tkinter.font.Font(
                            family="Poppins Bold", size=26, weight="normal"
                        )

                        # Configure Label Frame
                        self.configure(
                            bd=0, font=self.bold, text="Account " + str(account_num)
                        )
                        self.grid(row=row, column=0, pady=(15, 0), sticky=W)

                        # Account 1 - Active informations
                        self.account_active_informations_frame = LabelFrame(
                            self, text="Active informations:", bd=0
                        )

                        self.account_active_informations_frame.configure(
                            font=self.semibold
                        )
                        self.account_active_informations_frame.grid(
                            row=0, column=0, pady=(10, 0), sticky=NW
                        )

                        self.account_shadow_informations = Label(
                            self.account_active_informations_frame, text=""
                        )
                        self.account_shadow_informations.grid(
                            row=1, column=0, ipadx=150, sticky=NW
                        )

                        self.account_active_informations = Label(
                            self.account_active_informations_frame,
                            text=active_informations(account_num),
                            justify=LEFT,
                        )
                        self.account_active_informations.configure(font=self.normal)
                        self.account_active_informations.grid(row=1, column=0, sticky=W)

                        # Account 1 - Bot status
                        self.account_bot_status_frame = LabelFrame(
                            self, text="Bot status:", bd=0
                        )
                        self.account_bot_status_frame.configure(font=self.semibold)
                        self.account_bot_status_frame.grid(
                            row=0, column=1, pady=(10, 0), stick=NW, padx=(25, 0)
                        )

                        self.account_bot_status = Label(
                            self.account_bot_status_frame,
                            text="Waiting",
                            background="grey",
                        )
                        self.account_bot_status.configure(font=self.normal)
                        self.account_bot_status.grid(
                            row=1, column=1, pady=(10, 0), sticky=W, ipady=5, ipadx=150
                        )

                        # Account 1 - Short buttons
                        self.account_buttons_frame = LabelFrame(
                            self, text="Buttons:", bd=0
                        )
                        self.account_buttons_frame.configure(font=self.semibold)
                        self.account_buttons_frame.grid(
                            row=0, column=2, pady=(10, 0), sticky=NW, padx=(25, 0)
                        )

                        self.account_start_button = Button(
                            self.account_buttons_frame, text="Start bot"
                        )
                        self.account_start_button.configure(font=self.normal)
                        self.account_start_button.grid(
                            row=0, column=0, pady=(10, 0), sticky=W, ipady=10
                        )

                        self.account_stop_button = Button(
                            self.account_buttons_frame, text="Stop button"
                        )
                        self.account_stop_button.configure(font=self.normal)
                        self.account_stop_button.grid(
                            row=0, column=1, pady=(10, 0), sticky=W, ipady=10
                        )

                self.account_dict = dict()
                for i in range(1, 5):  # Store all 5 accounts in a dictionary
                    self.account_dict[i] = Account(self, int(i), int(i))

                for i in self.account_dict:  # Forget the grid
                    self.account_dict[i].forget()

            def show_accounts(self):  # Show the accounts
                self.configure(bd=0)
                self.grid(row=2, column=0)

        # Creating 2 types of class Accounts
        self.tiktok_accounts = Accounts(self, database.tiktok_active_informations)
        self.instagram_accounts = Accounts(self, database.instagram_active_informations)

        # Building dropdown menu
        self.accounts = {
            "TikTok": self.tiktok_accounts,
            "Instagram": self.instagram_accounts,
        }  # Create a dictionary

        # this is what the drop down menu displays
        self.selected = StringVar()

        # initialize the drop down menu
        self.selected.set("TikTok")
        self.accounts[self.selected.get()].show_accounts()

        # Show the accounts, but forgets the other one first
        def show():
            if self.selected.get() == "TikTok":
                self.accounts["Instagram"].grid_forget()
            else:
                self.accounts["TikTok"].grid_forget()

            self.accounts[self.selected.get()].show_accounts()

        # Drop down menu
        self.dropdown_menu = OptionMenu(
            self, self.selected, *self.accounts, command=lambda event: show()
        )
        self.dropdown_menu.grid(row=1, column=0, sticky=W)
