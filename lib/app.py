from kivymd.app import MDApp
from .home import MainWindow
from kivy.utils import QueryDict, rgba

# Create main app
class SocialBotApp(MDApp):
    colors = QueryDict()
    colors.black = rgba("#08090A")
    colors.black_cont = rgba("#121517")
    colors.red = rgba("#D90429")
    colors.gray = rgba("#D3D3D3")
    colors.white = rgba("#F5F5F5")
    colors.green = rgba("#0B6E4F")

    def build(self):
        return MainWindow()
