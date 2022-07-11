from tkinter import *
import tkinter.font
import pickle


class botSettings(Frame):
    def __init__(self, container):
        super().__init__(container)

        # Option menu function
        def toggle_accounts():
            if self.option_menu_string.get() == "Instagram":
                self.accounts["TikTok"].grid_forget()
                self.accounts["Instagram"].show_accounts()
            else:
                self.accounts["Instagram"].grid_forget()
                self.accounts["TikTok"].show_accounts()

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

        class SocialAccountSettings(LabelFrame):
            def __init__(self, container, social) -> None:
                super().__init__(container)

                class AccountSettings(LabelFrame):
                    def __init__(self, container, account_num, row) -> None:
                        super().__init__(container)

                        def update_auto_post():
                            self.temp_auto_post_dict = pickle.load(
                                open("auto_post_settings.pkl", "rb")
                            )
                            self.temp_auto_post_dict[
                                str(social) + str(account_num)
                            ] = self.i.get()
                            pickle.dump(
                                self.temp_auto_post_dict,
                                open("auto_post_settings.pkl", "wb"),
                                protocol=pickle.HIGHEST_PROTOCOL,
                            )

                        def update_bot_sleeping_time():
                            self.temp_auto_post_dict = pickle.load(
                                open("auto_post_settings.pkl", "rb")
                            )
                            self.temp_auto_post_dict[
                                "botsleeping" + str(social) + str(account_num)
                            ] = self.menu_values[self.menu_text.get()]
                            pickle.dump(
                                self.temp_auto_post_dict,
                                open("auto_post_settings.pkl", "wb"),
                                protocol=pickle.HIGHEST_PROTOCOL,
                            )

                        def update_menu_bot_sleeping_text():
                            for autopostkeys, autopostvalues in pickle.load(
                                open("auto_post_settings.pkl", "rb")
                            ).items():
                                if autopostkeys == "botsleeping" + str(social) + str(
                                    account_num
                                ):
                                    for (
                                        menukeys,
                                        menuvalues,
                                    ) in self.menu_values.items():
                                        if autopostvalues == menuvalues:
                                            return menukeys
                                else:
                                    pass

                        # Label Frame position
                        self.configure(bd=0)
                        self.grid(row=row, column=0, pady=15, padx=20, sticky=W)

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
                        self.account = Label(self, text="Account " + str(account_num))
                        self.account.configure(font=self.button)
                        self.account.grid(row=0, column=0)

                        # Checkbox
                        self.i = IntVar()
                        self.i.set(
                            int(
                                pickle.load(open("auto_post_settings.pkl", "rb"))[
                                    str(social) + str(account_num)
                                ]
                            )
                        )  # Update checkbutton
                        self.checkbox = Checkbutton(
                            self,
                            text="Auto post",
                            variable=self.i,
                            command=lambda: update_auto_post(),
                        )
                        self.checkbox.configure(font=self.normal)
                        self.checkbox.grid(row=0, column=1, padx=(500, 0))

                        # Text
                        self.sleeping_text = Label(self, text="The bot will sleep for")
                        self.sleeping_text.configure(font=self.normal)
                        self.sleeping_text.grid(row=0, column=2, padx=(50, 0))

                        # Posting delay
                        self.menu_text = StringVar()
                        self.menu_values = {
                            "1 Hour": 1,
                            "2 Hours": 2,
                            "3 Hours": 3,
                            "4 Hours": 4,
                            "5 Hours": 5,
                        }
                        self.menu_text.set(update_menu_bot_sleeping_text())
                        self.bot_sleeping_time = OptionMenu(
                            self,
                            self.menu_text,
                            *self.menu_values,
                            command=lambda event: update_bot_sleeping_time(),
                        )
                        self.bot_sleeping_time.configure(font=self.normal)
                        self.bot_sleeping_time.grid(row=0, column=3, padx=(10, 0))

                self.account_settings = []

                for i in range(1, 5):
                    self.account_settings.append(AccountSettings(self, i, i))

                self.configure(bd=0)

                self.grid_forget()

            def show_accounts(self):
                self.grid(row=1, column=0)

        self.accounts = {
            "TikTok": SocialAccountSettings(self.auto_post_frame, "TikTok"),
            "Instagram": SocialAccountSettings(self.auto_post_frame, "Instagram"),
        }

        # Option menu string var
        self.option_menu_string = StringVar()
        self.option_menu_string.set("TikTok")

        # Init which account to show
        self.accounts[self.option_menu_string.get()].show_accounts()

        # Option menu
        self.option_menu = OptionMenu(
            self.auto_post_frame,
            self.option_menu_string,
            *self.accounts,
            command=lambda event: toggle_accounts(),
        )
        self.option_menu.grid(row=0, column=0, pady=10, padx=(10, 0), sticky=W)
