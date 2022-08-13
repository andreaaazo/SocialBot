from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty
from kivy.lang import Builder

KV = """
<IconButton>:
    canvas.after:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
            source: self.source

"""
Builder.load_string(KV)

class IconButton(MDFlatButton):
    source = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
