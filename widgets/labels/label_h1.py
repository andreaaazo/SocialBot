from kivymd.uix.label import MDLabel
from kivy.lang import Builder as Bd


design = """
<LabelH1>:
    font_name: "assets/fonts/Poppins-Bold.ttf"
    font_size: "20sp"
"""
Bd.load_string(design)


class LabelH1(MDLabel):
    pass
