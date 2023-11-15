import os
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from mandel_layouts import ListItem

from app.utils.database import db_ref

class Item(ListItem):
    def on_click(self):
        ...

class List(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generate_list()

    def on_text_validate(self, query):
        self.generate_list(query)

    def generate_list(self, query=None):
        # container = self.ids.list_container
        # container.clear_widgets()
        print('generate_list')
        # data = db_ref.child('goods').get()
        # print(data)


file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'list.kv'))