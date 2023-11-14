import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from mandel_layouts import ListItem

class Item(ListItem):
    def on_click(self):
        ...

class List(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generate_list()

    def on_text_validate(self, query):
        self.generate_list(query)

    def generate_list(self, query=None):
        container = self.ids.list_container
        container.clear_widgets()




file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'list.kv'))

