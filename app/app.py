import imp
from multiprocessing.spawn import import_main_path
from kivymd.app import MDApp
from kivy.utils import QueryDict, rgba
from lib import MainWindow
from kivy.core.window import Window
from kivy.metrics import dp

# Minimum window size
Window.minimum_height = dp(500)
Window.minimum_width = dp(700)


# Create main app
class SocialBotApp(MDApp):
    colors = QueryDict()  # Define colors
    colors.black = rgba("#08090A")
    colors.black_cont = rgba("#121517")
    colors.red = rgba("#D90429")
    colors.gray = rgba("#D3D3D3")
    colors.white = rgba("#F5F5F5")
    colors.green = rgba("#0B6E4F")

    def build(self):
        return MainWindow()