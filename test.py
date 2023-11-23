from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
from kivy.utils import platform

from kivy.properties import ListProperty, StringProperty, NumericProperty
from app.utils.database import db_ref



if platform in ('win', 'macosx'):
    Window.size = (414, 736)

class Test(MDApp):
    title = 'My Mall'
    icon = 'app/icon.ico'

    # style
    header_bg_color = ListProperty([231 / 255, 225 / 255, 227 / 255, 1]) # 头部背景颜色
    main_bg_color = ListProperty([255 / 255, 255 / 255, 255 / 255, 1]) # 主体背景颜色
    bottom_bg_color = ListProperty([249 / 255, 245 / 255, 245 / 255, 1]) # 底部背景颜色
    main_btn_bg_color = ListProperty([251 / 255, 155 / 255, 42 / 255, 1]) # 主按钮背景颜色
    main_btn_font_color = ListProperty([255 / 255, 255 / 255, 255 / 255, 1]) # 主按钮字体颜色
    main_text_color = ListProperty([0 / 255, 0 / 255, 0 / 255, 0.88]) # 最深的文本色，默认的文本颜色
    tertiary_text_color = ListProperty([0 / 255, 0 / 255, 0 / 255, 0.45]) # 第三级文本色一般用于描述性文本，例如表单的中的补充说明文本、列表的描述性文本等场景。
    quaternary_text_color = ListProperty([0 / 255, 0 / 255, 0 / 255, 0.25]) # 第四级文本色是最浅的文本色，例如表单的输入提示文本
    placeholder_text_color = ListProperty([0 / 255, 0 / 255, 0 / 255, 0.25]) # 控制占位文本的颜色
    padding_xxs = NumericProperty(4) # 极小间距
    padding_xs = NumericProperty(8) # 特小间距
    padding_sm = NumericProperty(12) # 小间距
    padding_md = NumericProperty(18) # 中间距
    padding_lg = NumericProperty(24) # 大间距
    font_size_sm = NumericProperty(16) # 小号字体
    font_size = NumericProperty(24) # 标准字体
    font_size_md = NumericProperty(32) # 中号字体
    font_size_lg = NumericProperty(40) # 大号字体
    border_color = StringProperty('#d9d9d9') # 边框颜色
    test_color = ListProperty([222 / 255, 48 / 255, 35 / 255, 1]) # 测试颜色
    price_text_color = ListProperty([255 / 255, 68 / 255, 0 / 255, 1]) # 价格字体颜色

    def build(self):
        from app.screens import detail, login, register, update, navigator
        from app.widgets import cart, me, list
        from app.utils import MuskLayout

        self.muskLayout = MuskLayout()

        self.root = ScreenManager()

        self.cart = cart.Cart()
        self.detail = detail.Detail()
        self.list = list.List()
        self.login = login.Login()
        self.me = me.Me()
        self.register = register.Register()
        self.update = update.Update()
        self.navigator = navigator.Navigator()

        self.screens = {
            'cart': self.cart,
            'detail': self.detail,
            'list': self.list,
            'login': self.login,
            'me': self.me,
            'register': self.register,
            'update': self.update,
            'navigator': self.navigator
        }

        # self.root.switch_to(self.list)
        screen = Screen()

        # screen.add_widget(self.list) # <- widget测试专用(List, Cart, Me)

        self.root.add_widget(self.login) # <- screen测试请修改这里(Login, Register, Detail, Order, Update)

        return self.root
    
    def switch_screen(self, screen_name, direction='left'):
        self.root.transition.direction = direction
        self.root.switch_to(self.screens.get(screen_name))
    
    def get_screen(self, screen_name):
        return self.screens.get(screen_name)

if __name__ == '__main__':
    Test().run()

