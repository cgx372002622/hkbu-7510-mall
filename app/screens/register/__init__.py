import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from app.utils.database import db_ref




class Register(Screen):
    def register(self):
        dialog = MDDialog(
            title = 'Successful registration',
            text = 'This is your personal information',
            buttons = [
                MDRaisedButton(
                    text = 'Complete Registration',
                    on_press = lambda x: dialog.dismiss(),
                    on_release = lambda y: MDApp.get_running_app().switch_screen("login")
                    ),
            ]
        )
        dialog.open()

    def cancel(self):
        self.ids.text_username.text = ''
        self.ids.text_password.text = ''
        self.ids.text_nickname.text = ''
        self.ids.text_phoneNumber.text = ''
        self.ids.text_address.text = ''

    def submit_data(self):
        username = self.ids.text_username.text
        password = self.ids.text_password.text
        nickname = self.ids.text_nickname.text
        phoneNumber = self.ids.text_phoneNumber.text
        address = self.ids.text_address.text

        data = {
            'username': username,
            'password': password,
            'nickname': nickname,
            'phoneNumber': phoneNumber,
            'address': address,
        }

        users_ref = db_ref.child('users')
        users_ref.push(str(data))

        self.ids.text_nickname.text = ''
        self.ids.text_password.text = ''
        self.ids.text_nickname.text = ''
        self.ids.text_phoneNumber.text = ''
        self.ids.text_address.text = ''

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'register.kv'))

