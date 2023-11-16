import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

class Login(Screen):
    
    def register(self):
        dialog = MDDialog(
            title = 'Successful registration', 
            text = 'This is your personal information',
            buttons = [
                MDRaisedButton(
                    text = 'Complete Registration',
                    on_press = lambda: dialog.dismiss(),
                    ),
            ]
        )
        dialog.open()

        
        
        
        
        
        dialog2 = MDDialog(
            title = 'Warning',
            text = 'the password and re-enter password are differenty'
        )


file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'login.kv'))

