from kivymd.uix.button import MDTextButton
from kivy.lang import Builder

KV = """
<NavBarUpTextBtn>:
    font_name: "assets/fonts/Poppins-Medium.ttf"
    font_size: "12dp"
    color: app.colors.gray
    pos_hint: {"center_y" : .5}
""" 
Builder.load_string(KV)

class NavBarUpTextBtn(MDTextButton):
    pass

