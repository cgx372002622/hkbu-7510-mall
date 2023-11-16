import os
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.list.list import ThreeLineAvatarListItem, ImageLeftWidget

from kivymd.app import MDApp

from app.utils.database import db_ref

class Item(ThreeLineAvatarListItem):
    pass

class List(BoxLayout):

    app = MDApp.get_running_app()

    def initiation(self):
        self.generate_list()

    def on_text_validate(self, query):
        self.generate_list(query)

    def generate_list(self, query=None):
        container = self.ids.get('list_container')
        container.clear_widgets()
        data = None
        if query is None or query.strip() == '':
            data = db_ref.child('goods').get()
        else:
            data = db_ref.child('goods').order_by_child('name').equal_to(query).get()
        for k in data.keys():
            d = data[k]
            item = Item(
                ImageLeftWidget(
                    source = d.get('picUrl')
                ),
                id = d.get('id'),
                text = d.get('name'),
                secondary_text = str(d.get('price')),
                tertiary_text = d.get('store'),
                on_press= lambda x: self.app.get_screen('detail').init_item(x.id),
                on_release = lambda x: self.app.switch_screen('detail')
            )
            container.add_widget(item)

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'list.kv'))