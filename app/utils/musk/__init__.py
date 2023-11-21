from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.spinner import MDSpinner
from kivymd.app import MDApp

class MuskLayout(MDFloatLayout):
    def __init__(self, **kargs):
        super(MuskLayout, self).__init__(**kargs)
        self.spinner = MDSpinner(
            size_hint=[.2, .2],
            pos_hint={'center_x': .5, 'center_y': .5},
            active=True
        )
        self.size_hint = [1, 1]
        self.md_bg_color = MDApp.get_running_app().main_bg_color
        self.add_widget(self.spinner)

    def show(self, screen):
        screen.add_widget(self)

    def hide(self, screen):
        screen.remove_widget(self)