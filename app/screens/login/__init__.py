import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from app.utils.database import db_ref
from kivymd.uix.dialog import MDDialog
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivymd.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivymd.uix.label import MDLabel
from kivy.uix.popup import Popup
from app.Global import appData
from app.components import SpinnerDialog

from kivy.core.text import LabelBase
LabelBase.register(name='Disko-1', fn_regular='app/resources/Roboto-Bold.ttf')


class Login(Screen):
        
    spinnerDialog = SpinnerDialog()

    def login(self):
        self.spinnerDialog.show()
        Clock.schedule_once(lambda x: self.login_vertify(), 0.5)
        Clock.schedule_once(lambda x: self.spinnerDialog.hide(), 1)

    def login_vertify(self):
        username = self.ids.text_username.text
        password = self.ids.text_password.ids.text_field.text

        if not username or not password:
            dialog3 = MDDialog(
                title='Warning',
                text='Please enter both username and password.',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog3.dismiss(),
                    )
                ]
            )
            dialog3.open()
            return

        users_ref = db_ref.child('users')
        query_result = users_ref.order_by_child('username').get()

        user_exists = False  #追踪是否找到匹配的用户名和密码
        query_username = None

        if query_result:
            for result in query_result.values():
                query_username = result['username']
                #query_password = result['password']
                if query_username == username:
                    user_exists = True
                    break
                
        if user_exists:
            query_password = result['password']
            if query_password == password:
                username = self.ids.text_username.text

                appData.init_user(username) # 在Global中存入当前用户信息，username、nickname、address、phoneNumber
                
                MDApp.get_running_app().switch_screen("navigator")
                self.ids.text_username.text = ''
                self.ids.text_password.ids.text_field.text = ''
                #self.show_success_popup()

            else:
                query_username != username or query_password != password
                dialog1 = MDDialog(
                            title = 'Warning',
                            text = 'Password incorrect!',
                            buttons = [
                                MDRaisedButton(
                                    text = 'Return',
                                    on_press = lambda x: dialog1.dismiss(),
                                )
                            ]
                        )
                dialog1.open()

        else:
            dialog2 = MDDialog(
                title='Warning',
                text='Username does not exist. Please register.',
                buttons=[
                    MDRaisedButton(
                        text='Register',
                        on_press=lambda x: dialog2.dismiss(),
                        on_release = lambda x: MDApp.get_running_app().switch_screen("register"),
                        
                    ),
                    MDRaisedButton(
                        text='Cancel',
                        on_press=lambda x: dialog2.dismiss(),
                        
                    )
                ]
            )
            dialog2.open()
             

    # def show_success_popup(self):
    #         layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    #         label = Label(text='Login successful!')

    #         popup = Popup(title='Success', content=layout, size_hint=(None, None), size=(300, 200))
    #         layout.add_widget(label)

    #         popup.open()
    #         Clock.schedule_once(lambda dt: popup.dismiss(), 2)

    def clean(self):
        self.ids.text_username.text = ''
        self.ids.text_password.ids.text_field.text = ''

    

class ClickableTextFieldRound1(Screen):
    text = StringProperty()
    


    



file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'login.kv'))



