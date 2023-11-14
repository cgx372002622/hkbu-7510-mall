from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from kivy.core.window import Window
from kivy.utils import platform

### Set window size if the app runs on Windows or MacOS
if platform in ('win', 'macosx'):
    Window.size = (414, 736)

from .Global import appData

class Mall(MDApp):
    def build(self):
        self.title = 'MyMall'

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