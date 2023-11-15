import os
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class Me(BoxLayout):
    pass

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'me.kv'))