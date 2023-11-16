import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

class Detail(Screen):
    app = MDApp.get_running_app()
    
    def init_item(self, id):
        self.detail_title = id

    def go_back(self):
        self.app.switch_screen('navigator', 'right')

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'detail.kv'))

