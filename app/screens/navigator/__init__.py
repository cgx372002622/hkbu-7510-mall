import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class Navigator(Screen):
    pass

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'navigator.kv'))