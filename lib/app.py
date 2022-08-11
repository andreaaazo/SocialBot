from kivymd.app import MDApp
from .home import *

# Create main app
class SocialBotApp(MDApp):
    def build(self):
        return MainWindow()
