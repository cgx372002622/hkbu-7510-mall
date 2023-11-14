from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from kivy.core.window import Window
from kivy.utils import platform

from kivy.properties import ListProperty, StringProperty, NumericProperty

### Set window size if the app runs on Windows or MacOS
if platform in ('win', 'macosx'):
    Window.size = (414, 736)

from .Global import appData

class Mall(MDApp):
    title = 'My Mall'
    icon = 'app/icon.ico'

    # style
    header_bg_color = ListProperty([249 / 255, 245 / 255, 245 / 255, 1]) # 头部背景颜色
    main_bg_color = ListProperty([255 / 255, 255 / 255, 255 / 255, 1]) # 主体背景颜色
    main_btn_bg_color = ListProperty([251 / 255, 155 / 255, 42 / 255, 1]) # 主按钮背景颜色
    main_btn_font_color = ListProperty([255 / 255, 255 / 255, 255 / 255, 1]) # 主按钮字体颜色
    main_text_color = ListProperty([0 / 255, 0 / 255, 0 / 255, 1]) # 最深的文本色
    border_color = '#d9d9d9' # 边框颜色

    def build(self):
        from .screens import cart, detail, list, login, me, register

        self.root = ScreenManager()

        self.cart = cart.Cart()
        self.detail = detail.Detail()
        self.list = list.List()
        self.login = login.Login()
        self.me = me.Me()
        self.register = register.Register()

        self.screens = {
            'cart': self.cart,
            'detail': self.detail,
            'list': self.list,
            'login': self.login,
            'me': self.me,
            'register': self.register
        }

        self.root.switch_to(self.login)

        return self.root
    
    def switch_screen(self, screen_name, direction='left'):
        self.root.transition.direction = direction
        self.root.switch_to(self.screens.get(screen_name))