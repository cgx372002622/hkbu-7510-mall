import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
import threading

from app.utils import db_ref

class Detail(Screen):
    app = MDApp.get_running_app()
    add_in_cart_dialog = None
    make_a_comment_dialog = None

    def init_item(self, id):
        self.detail_title = id

    def go_back(self):
        self.app.switch_screen('navigator', 'right')

    def add_in_cart(self):
        if not self.add_in_cart_dialog:
            self.add_in_cart_dialog = MDDialog(
                text = 'Add In Cart Successfully!',
                buttons = [],
                radius = [20, 20, 20, 20]
            )
        self.add_in_cart_dialog.open()
        threading.Timer(1, self.add_in_cart_dialog.dismiss).start()

    def make_a_comment(self):
        comment_field = self.ids.comment
        comment = comment_field.text
        if not comment or comment.strip() == '':
            comment_field.helper_text_mode = 'on_error'
            comment_field.helper_text = 'comment should not be empty!'
            comment_field.error = True
        else:
            if not self.make_a_comment_dialog:
                self.make_a_comment_dialog = MDDialog(
                    text = 'Make a comment Successfully!',
                    buttons = [],
                    radius = [20, 20, 20, 20]
                )
            self.make_a_comment_dialog.open()
            threading.Timer(1, self.make_a_comment_dialog.dismiss).start()
            self.ids.comment.text = ''
            self.render_comment()

    def render_comment(self):
        ...

    def comment_on_focus(self, instance, status):
        if not status:
            instance.error = False

    def go_buy(self):
        ...

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'detail.kv'))

