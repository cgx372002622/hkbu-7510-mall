import os
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class Cart(BoxLayout):
    pass

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'cart.kv'))