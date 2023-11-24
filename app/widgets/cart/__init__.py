import os
import threading
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog

from app.utils import db_ref
from app.Global import appData
from app.components import SpinnerDialog

class DeleteBtn(MDIconButton):
    item_id = None
    def __init__(self, item_id='', **kwargs):
        super(DeleteBtn, self).__init__(**kwargs)
        self.item_id = item_id

class Empty(MDBoxLayout):
    pass

class ItemContent(ButtonBehavior, MDBoxLayout):

    def __init__(self, item_id='', item_name='', item_price='', item_store='', picUrl='', goods_count='', item_key='', **kwargs):
        super(ItemContent, self).__init__(**kwargs)
        self.goods_name = item_name
        self.goods_store = item_store
        self.goods_price = item_price
        self.goods_id = item_id
        self.picUrl = picUrl
        self.goods_count = goods_count
        self.item_key = item_key

    def go_detail(self, itemId):
        print('go_detail')
        app = MDApp.get_running_app()
        app.get_screen('detail').init_item(itemId)
        app.switch_screen('detail')

    def add_count(self):
        item_ref = db_ref.child('users/' + appData.current_userId + '/cart/' + self.item_key)
        cur_count = item_ref.child('count').get()
        item_ref.update({'count': cur_count + 1})
        ready_passed_cart = appData.ready_passed_cart
        for i in ready_passed_cart:
            if i['key'] == self.item_key:
                i['count'] = i['count'] + 1

    def minus_count(self, goods_count):
        if int(goods_count.text) > 0:
            goods_count.text = str(int(goods_count.text) - 1)
            item_ref = db_ref.child('users/' + appData.current_userId + '/cart/' + self.item_key)
            cur_count = item_ref.child('count').get()
            item_ref.update({'count': cur_count - 1})
            ready_passed_cart = appData.ready_passed_cart
            for i in ready_passed_cart:
                if i['key'] == self.item_key:
                    i['count'] = i['count'] - 1

    def do_nothing(self):
        print('do_nothing')
        print(self.item_key)
        
class ItemCheck(MDCheckbox):
    item_id = None
    def __init__(self, item_id='', **kwargs):
        super(ItemCheck, self).__init__(**kwargs)
        self.item_id = item_id

class CartItem(MDCard):
    pass

class Cart(MDBoxLayout):
    empty_notice = None

    def initiation(self):
        self.render_list()

    def clear(self):
        if self.cartItem_box is None:
            self.cartItem_box = self.ids.item_box
        self.itemChecks.clear()
        self.cartItem_box.clear_widgets()
        self.ready_passed_cart = []
        self.itemChecks = []

    def render_list(self):
        spinnerDialog = SpinnerDialog()
        spinnerDialog.show()

        Clock.schedule_once(lambda x: self.generate_list(), 0.5)

        Clock.schedule_once(lambda x: spinnerDialog.hide(), 1)

    def generate_list(self):
        if self.cartItem_box is None:
            self.cartItem_box = self.ids.item_box

        # 初始化
        self.itemChecks.clear()
        self.cartItem_box.clear_widgets()
        appData.ready_passed_cart = []
        select_all_box = self.ids.select_all_box
        select_all_box.active = False

        cart_obj = db_ref.child('users/' + appData.current_userId + '/cart').get()

        if cart_obj is None:
            # 渲染empty
            self.cartItem_box.add_widget(Empty())
        else:
            for k, v in cart_obj.items():
                item_id = k
                goods_id = v['goodsId']
                count = v['count']
                self.ready_passed_cart.append({
                    'goods_id': goods_id,
                    'count': count,
                    'key': item_id
                })
                goods = db_ref.child('goods/' + goods_id).get()
                item_check = ItemCheck(item_id=item_id)
                cart_item = CartItem(
                    MDBoxLayout(
                        item_check,
                        MDBoxLayout(
                            size_hint=(1, 0.6)
                        ),
                        DeleteBtn(
                            item_id=item_id,
                            icon='delete-circle', 
                            theme_text_color='Custom', 
                            text_color=MDApp.get_running_app().secondary_btn_bg_color, 
                            size_hint=(1, 0.2),
                            on_press=lambda x: self.delete_on_press(x.item_id)
                        ),
                        orientation='vertical',
                        size_hint=(.1, 1),
                ), ItemContent(
                    item_id=goods['id'],
                    item_name=goods['name'],
                    item_price=str(goods['price']),
                    item_store=goods['store'],
                    picUrl=goods['picUrl'],
                    goods_count=str(count),
                    item_key=item_id
                ))
                self.itemChecks.append(item_check)
                self.cartItem_box.add_widget(cart_item)
            appData.ready_passed_cart = self.ready_passed_cart

    def go_buy(self):
        checked_number = 0
        for i in self.itemChecks:
            if i.active:
                checked_number += 1
        if not self.empty_notice:
            self.empty_notice = MDDialog(
                text="Please select at least one item.",
                buttons=[]
            )
        if checked_number == 0:
            self.empty_notice.open()
            threading.Timer(1, self.empty_notice.dismiss).start()
        else:
            for i in self.itemChecks:
                if i.active:
                    key = i.item_id
                    count = 0
                    goods_id = ''
                    for i in self.ready_passed_cart:
                        if i['key'] == key:
                            count = i['count']
                            goods_id = i['goods_id']
                            break
                    appData.passed_cart.append({
                        'key': key,
                        'count': count,
                        'goods_id': goods_id
                    })
            print(appData.passed_cart)
            MDApp.get_running_app().switch_screen('check', 'left')

    def delete_on_press(self, item_id):
        item_ref = db_ref.child('users/' + appData.current_userId + '/cart/' + item_id)
        item_ref.delete()
        self.render_list()

    def select_all_change(self, checkbox):
        is_all_selected = checkbox.active
        
        for i in self.itemChecks:
            i.active = is_all_selected

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'cart.kv'))