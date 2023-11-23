import os
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import AsyncImage
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock

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

class RoundedImage(AsyncImage):
    pass

class ItemContent(ButtonBehavior, MDBoxLayout):

    def __init__(self, item_id='', item_name='', item_price='', item_store='', picUrl='', **kwargs):
        super(ItemContent, self).__init__(**kwargs)
        self.goods_name = item_name
        self.goods_store = item_store
        self.goods_price = item_price
        self.goods_id = item_id
        self.picUrl = picUrl

    def go_detail(self, itemId):
        print('go_detail')
        app = MDApp.get_running_app()
        app.get_screen('detail').init_item(itemId)
        app.switch_screen('detail')
class ItemCheck(MDCheckbox):
    pass

class CartItem(MDBoxLayout):
    pass

class Cart(MDBoxLayout):

    def initiation(self):
        self.render_list()

    def clear(self):
        if self.cartItem_box is None:
            self.cartItem_box = self.ids.item_box
        self.itemChecks.clear()
        self.cartItem_box.clear_widgets()

    def render_list(self):
        spinnerDialog = SpinnerDialog()
        spinnerDialog.show()

        Clock.schedule_once(lambda x: self.generate_list(), 0.5)

        Clock.schedule_once(lambda x: spinnerDialog.hide(), 1)

    def generate_list(self):
        if self.cartItem_box is None:
            self.cartItem_box = self.ids.item_box
        self.itemChecks.clear()
        self.cartItem_box.clear_widgets()

        cart_obj = db_ref.child('users/' + appData.current_userId + '/cart').get()

        if cart_obj is None:
            # 渲染empty
            self.cartItem_box.add_widget(Empty())
        else:
            for k, v in cart_obj.items():
                item_id = k
                goods_id = v['goodsId']
                goods = db_ref.child('goods/' + goods_id).get()
                item_check = ItemCheck()
                cart_item = CartItem(
                    MDBoxLayout(
                        item_check,
                        MDBoxLayout(
                            size_hint=(1, 0.6)
                        ),
                        DeleteBtn(
                            item_id=item_id,
                            icon='delete', 
                            theme_text_color='Custom', 
                            text_color=(1, 0, 0, 1), 
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
                    picUrl=goods['picUrl']
                ))
                self.itemChecks.append(item_check)
                self.cartItem_box.add_widget(cart_item)

    def go_buy(self):
        ...

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