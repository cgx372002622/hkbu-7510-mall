import os
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.list.list import ThreeLineAvatarListItem, ImageLeftWidget
from kivymd.app import MDApp
from app.Global import appData

class Me(BoxLayout):
    # def display_userdata(self):
    username = appData.current_username
    nickname = appData.current_nickname
    phonenumber = appData.current_phoneNumber
    address = appData.current_phoneNumber

    # def Get_username():
   

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'me.kv'))