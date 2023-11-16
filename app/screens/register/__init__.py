import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

class Register(Screen):
    def register(self):
        dialog = MDDialog(
            title = 'Successful registration',
            text = 'This is your personal information',
            buttons = [
                MDRaisedButton(
                    text = 'Complete Registration',
                    on_press = lambda x: dialog.dismiss(),
                    ),
            ]
        )
        dialog.open()

    def cancel(self):
        self.ids.text_username.text = ''
        self.ids.text_password.text = ''
        self.ids.text_phone_number.text = ''
        self.ids.text_address.text = ''

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'register.kv'))

