import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
import threading
from kivymd.app import MDApp

from app.utils import db_ref
from app.Global import appData
from app.components import SpinnerDialog

class Address(MDCard):
    def __init__(self, current_user_address='', **kwargs):
        super(Address, self).__init__(**kwargs)
        self.current_user_address = current_user_address

class Phone(MDCard):
    def __init__(self, current_user_phonenumber='', **kwargs):
        super(Phone, self).__init__(**kwargs)
        self.current_user_phonenumber = current_user_phonenumber

class CheckItem(MDCard):
    def __init__(self, goods_count='', goods_name='', goods_price='', goods_store='', goods_pic_url='', **kwargs):
        super(CheckItem, self).__init__(**kwargs)
        self.goods_count = goods_count
        self.goods_name = goods_name
        self.goods_price = goods_price
        self.goods_store = goods_store
        self.goods_pic_url = goods_pic_url

class Check(Screen):
    success_notice = None

    def on_enter(self):
        self.current_user_address = appData.current_address
        self.current_user_phonenumber = appData.current_phoneNumber
        self.spinnerDialog = SpinnerDialog()
        self.render_list()

    def on_leave(self):
        self.total_price = ''
        goods_box = self.ids.goods_box
        goods_box.clear_widgets()
        appData.passed_cart = []

    def render_list(self):
        self.spinnerDialog.show()
        Clock.schedule_once(lambda x: self.generate_list(), 0.5)
        Clock.schedule_once(lambda x: self.spinnerDialog.hide(), 1)

    def generate_list(self):
        passed_cart = appData.passed_cart
        goods_box = self.ids.goods_box
        total_price = 0
        goods_box.add_widget(Address(current_user_address=appData.current_address))
        goods_box.add_widget(Phone(current_user_phonenumber=appData.current_phoneNumber))
        for i in passed_cart:
            goods_id = i['goods_id']
            count = i['count']
            goods = db_ref.child('goods/' + goods_id).get()
            goods_name = goods['name']
            goods_price = goods['price']
            total_price += (int(goods_price) * int(count))
            goods_store = goods['store']
            goods_pic_url = goods['picUrl']
            check_item = CheckItem(
                goods_count=str(count),
                goods_name=goods_name,
                goods_price=str(goods_price),
                goods_store=goods_store,
                goods_pic_url=goods_pic_url,
            )
            goods_box.add_widget(check_item)
        self.total_price = str(total_price)

    def check(self):
        if not self.success_notice:
            self.success_notice = MDDialog(
                text="Payment successful",
                buttons=[]
            )
        self.post_handle()
        self.success_notice.open()
        threading.Timer(1, self.success_notice.dismiss).start()
        Clock.schedule_once(lambda x: self.go_back(), 1.5)

    # 删掉购物车里对应的物品
    def post_handle(self):
        passed_cart = appData.passed_cart
        for i in passed_cart:
            key = i['key']
            item_ref = db_ref.child('users/' + appData.current_userId + '/cart/' + key)
            item_ref.delete()

    def go_back(self):
        MDApp.get_running_app().switch_screen('navigator', 'right')
    

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'check.kv'))