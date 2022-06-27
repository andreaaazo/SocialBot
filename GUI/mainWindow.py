from .dashboard import dashboard
from .accounts import *
from .freeProxy import *
from .userProxy import *
from .botSettings import *


class mainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720+0+0")
        self.title("Socialbot by @andreaaa.zo & @lukesafes")

        # memberwise variables
        self.freeProxy = freeProxy(self)
        self.dashboard = dashboard(self)
        self.userProxy = userProxy(self)
        self.botSettings = botSettings(self)
        self.dashboard.pack()  # Show dashboard at beginning

        self.x = dict()  # creating memberwise accounts variables
        for i in range(1, 5):
            self.x[i] = account(self, i)

        def show_dashboard():
            forget_all_frames()
            self.dashboard.pack()

        def show_account(i):
            forget_all_frames()
            self.x[i].pack()

        def show_free_proxy():
            forget_all_frames()
            self.freeProxy.pack()

        def show_bot_settings():
            forget_all_frames()
            self.botSettings.pack()

        def show_user_proxy():
            forget_all_frames()
            self.userProxy.pack()

        def forget_all_frames():
            self.freeProxy.pack_forget()
            self.botSettings.pack_forget()
            self.userProxy.pack_forget()
            self.dashboard.pack_forget()
            for i in self.x:
                self.x[i].pack_forget()

        # menu config
        self.mainMenu = Menu(self)
        self.config(menu=self.mainMenu)
        self.accountManagerMenu = Menu(self.mainMenu)
        self.proxiesMenu = Menu(self.mainMenu)
        self.botSettingsMenu = Menu(self.mainMenu)

        # Account Manager Menu
        self.mainMenu.add_cascade(label="Account Manager", menu=self.accountManagerMenu)

        self.accountManagerMenu.add_command(label="Dashboard", command=show_dashboard)

        for i in self.x:  # create menu commands account stored in dict
            self.accountManagerMenu.add_command(
                label="Account " + str(i), command=lambda i=i: show_account(i)
            )

        # Proxies Menu
        self.mainMenu.add_cascade(label="Proxies", menu=self.proxiesMenu)

        self.proxiesMenu.add_command(label="Free Proxy", command=show_free_proxy)

        self.proxiesMenu.add_command(label="User Proxy", command=show_user_proxy)

        # Bot Settings Menu
        self.mainMenu.add_cascade(label="Bot", menu=self.botSettingsMenu)

        self.botSettingsMenu.add_command(label="Settings", command=show_bot_settings)
