import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
import threading
from datetime import datetime

from app.utils import db_ref, spinnerMusk
from app.Global import appData

class Comment(MDBoxLayout):
    def __init__(self, content=None, time=None, username=None, **kwargs):
        super(Comment, self).__init__(**kwargs)
        self.content = content
        self.time = time
        self.username = username

class Detail(Screen):
    app = MDApp.get_running_app()
    add_in_cart_dialog_success = None
    add_in_cart_dialog_existed = None
    make_a_comment_dialog = None
    musk_layout = None

    def init_item(self, id):
        self.detail_id = id

    def on_pre_enter(self):
        spinnerMusk.show(self)

    def on_enter(self):
        detail = db_ref.child('goods/' + self.detail_id).get()
        self.picUrl = detail.get('picUrl')
        self.price = str(detail.get('price'))
        self.detail_name = detail.get('name')
        self.store = detail.get('store')
        self.description = detail.get('description')
        self.render_comment()
        spinnerMusk.hide(self)

    def on_leave(self):
        self.picUrl = ''
        self.price = ''
        self.detail_name = ''
        self.store = ''
        self.description = ''
        comment_box = self.ids.comment_box
        comment_box.clear_widgets()


    def go_back(self):
        self.app.switch_screen('navigator', 'right')

    def add_in_cart(self):
        if not self.add_in_cart_dialog_success:
            self.add_in_cart_dialog_success = MDDialog(
                text = 'Add In Cart Successfully!',
                buttons = [],
                radius = [20, 20, 20, 20]
            )
        if not self.add_in_cart_dialog_existed:
            self.add_in_cart_dialog_existed = MDDialog(
                text = 'This item has been existed in your cart!',
                buttons = [],
                radius = [20, 20, 20, 20]
            )
        cart_ref = db_ref.child('users/' + appData.current_userId + '/cart')
        cart = cart_ref.get()
        if cart is None:
            cart_ref.push({
                'goodsId': self.detail_id,
                'count': 1
            })
            self.add_in_cart_dialog_success.open()
            threading.Timer(1, self.add_in_cart_dialog_success.dismiss).start()
        else:
            is_exist = False
            for k, v in cart.items():
                if v['goodsId'] == self.detail_id:
                    is_exist = True
                    break
            if is_exist:
                self.add_in_cart_dialog_existed.open()
                threading.Timer(1.5, self.add_in_cart_dialog_existed.dismiss).start()
            else:
                cart_ref.push({
                    'goodsId': self.detail_id,
                    'count': 1
                })
                self.add_in_cart_dialog_success.open()
                threading.Timer(1, self.add_in_cart_dialog_success.dismiss).start()

    def make_a_comment(self):
        comment_field = self.ids.comment
        comment = comment_field.text
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
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
            db_ref.child('goods/' + self.detail_id + '/comments').push({
                'username': appData.current_nickname,
                'time': formatted_time,
                'content': comment
            })
            self.render_comment()

    def render_comment(self):
        comments = db_ref.child('goods/' + self.detail_id + '/comments').order_by_child('time').get()
        if not comments:
            self.comments = {}
        else:
            self.comments = comments
        comment_box = self.ids.comment_box
        comment_box.clear_widgets()

        if comments:
            i = 1
            for k in self.comments.keys():
                c = self.comments[k]
                time = c.get('time')
                username = c.get('username')
                content = c.get('content')
                comment = Comment(
                    content = str(i) + '. ' + content,
                    time = time,
                    username = username
                )
                comment_box.add_widget(comment)
                i = i + 1
        else:
            comment_box.add_widget(MDLabel(
                text='Add your first comment!',
                theme_text_color='Custom',
                text_color=self.app.tertiary_text_color,
                pos_hint={'x': .2}
            ))

    def comment_on_focus(self, instance, status):
        if not status:
            instance.error = False

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'detail.kv'))

