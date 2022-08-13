from kivymd.uix.label import MDLabel
from kivy.lang import Builder as Bd


design = """
<LabelH1>:
    font_name: "assets/fonts/Poppins-Bold.ttf"
    font_size: int((root.width + root.height) / 9)
"""
Bd.load_string(design)


class LabelH1(MDLabel):
    pass
