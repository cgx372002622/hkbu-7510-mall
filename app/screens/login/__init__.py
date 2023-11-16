import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from app.utils.database import db_ref


class Login(Screen):


    def login_vertify(self):
        pass




file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'login.kv'))

