import os
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from app.Global import appData

class Me(MDBoxLayout):
    
    def initiation(self):
        self.username = appData.current_username
        self.nickname = appData.current_nickname
        self.phonenumber = appData.current_phoneNumber
        self.address = appData.current_phoneNumber

    # def Get_username():
   

file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'me.kv'))