from tkinter import *
import tkinter.font


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

        # Auto post title
        self.auto_post_frame = Label(self.body_frame, text="Auto post settings", bd=0)
        self.auto_post_frame.configure(font=self.semibold)
        self.auto_post_frame.grid(row=0, column=0, padx=(20, 0))

        class SocialAccounts(LabelFrame):
            def __init__(self, master):
                super().__init__(master)

                class Account(LabelFrame):
                    def __init__(self, account_num, row):
                        super().__init__()
                        self.grid(row=row, column=0)

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
                        self.bold = tkinter.font.Font(
                            family="Poppins Bold", size=26, weight="normal"
                        )

                        # Account Label
                        self.account = Label(self, text="Account" + str(account_num))
                        self.account.configure(font=self.semibold)
                        self.account.grid(row=0, column=0, pady=(15, 0), padx=(20, 0))

                        # Checkbox
                        self.i = IntVar()
                        self.checkbox = Checkbutton(
                            self,
                            text="Auto post",
                            variable=self.i,
                            command=lambda: print(self.i.get()),
                        )
                        self.checkbox.configure(font=self.normal)
                        self.checkbox.grid(row=0, column=1, padx=(50, 0), pady=(15, 0))

                        # Text
                        self.sleeping_text = Label(self, text="The bot will sleep for")
                        self.sleeping_text.configure(font=self.normal)
                        self.sleeping_text.grid(
                            row=0, column=2, padx=(100, 5), pady=(15, 0)
                        )

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
                            self, self.menu_text, *self.menu_values
                        )
                        self.bot_sleeping_time.configure(font=self.normal)
                        self.bot_sleeping_time.grid(row=0, column=3, pady=(15, 0))

                self.accounts = []
                for i in range(1, 5):
                    self.accounts.append(Account(i, i).forget())

                # for i in self.accounts:
                # self.accounts[i].show()

            def show_accounts(self):
                self.grid(row=1, column=0)

        self.instagram = SocialAccounts(self.body_frame)
