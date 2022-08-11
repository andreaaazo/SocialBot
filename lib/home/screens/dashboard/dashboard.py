from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty


class Dashboard(MDScreen):
    text = StringProperty("I'm the dashboard!")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
