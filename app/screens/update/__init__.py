import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from app.Global import appData
from firebase_admin import db
from kivy.clock import Clock
from kivymd.app import MDApp

class Update(Screen): 
    password=appData.current_password

    def on_enter(self):
        self.ids.txt_NewNickname.text = appData.current_nickname
        self.ids.txt_NewPhoneNumber.text = appData.current_phoneNumber
        self.ids.txt_NewAddress.text = appData.current_address

    def cancel(self):   #清理全部文本
        self.ids.txt_OldPassword.text = ''
        self.ids.txt_NewPassword.text = ''
        self.ids.txt_ConfirmNewPassword.text = ''
        self.ids.txt_NewNickname.text = ''
        self.ids.txt_NewPhoneNumber.text = ''
        self.ids.txt_NewAddress.text = ''
    
    def verify(self):   #判断输入的文本是否有问题（密码不一致或者是否有空的），没问题就上传更新用户数据
        # 填了确认新密码，没填新密码，提示
        if (self.ids.txt_NewPassword.text != '' and self.ids.txt_OldPassword.text == ''):
            dialog = MDDialog(
                title='Retry',
                text='Please enter old password!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog.dismiss(),
                    )
                ]
            )
            dialog.open()
        # 填了新密码，没填旧密码，提示
        elif (self.ids.txt_ConfirmNewPassword.text != '' and self.ids.txt_NewPassword.text == ''):
            dialog = MDDialog(
                title='Retry',
                text='Please enter new password!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog.dismiss(),
                    )
                ]
            )
            dialog.open()
        # 填了确认旧密码，没填新密码，提示
        elif (self.ids.txt_OldPassword.text != '' and self.ids.txt_NewPassword.text == ''):
            dialog = MDDialog(
                title='Retry',
                text='Please enter new password',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog.dismiss(),
                    )
                ]
            )
            dialog.open()
        # 填了新密码，没填确认新密码，提示
        elif self.ids.txt_NewPassword.text != '' and self.ids.txt_ConfirmNewPassword.text == '':    
            dialog = MDDialog(
                title='Retry',
                text='Please enter confirmed new password!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog.dismiss(),
                    )
                ]
            )
            dialog.open()
        # 填了旧密码，但密码与数据库不一致，提示 
        elif self.ids.txt_OldPassword.text != '' and self.ids.txt_OldPassword.text != appData.current_password:
                
            dialog = MDDialog(
                title='Retry',
                text='Please enter correct old password!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog.dismiss(),
                    )
                ]
            )
            dialog.open()
        # 填了旧密码，但新密码与确认新密码不一致，提示 
        elif self.ids.txt_OldPassword.text != '' and self.ids.txt_NewPassword.text != self.ids.txt_ConfirmNewPassword.text:
            dialog = MDDialog(
                title='Retry',
                text='The new password is different from the confirmed password!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog.dismiss(),
                    )
                ]
            )
            dialog.open() 
        else : # 上传到firebase更新用户数据
            users_ref = db.reference('users')
            query = users_ref.order_by_child('username').equal_to(appData.current_username)
            results = query.get()

            user_id = next(iter(results.keys()))
            user_ref = users_ref.child(user_id)

            new_data = None
            
            if self.ids.txt_OldPassword.text != '':
                # 改了密码
                new_data = {
                    'address':     self.ids.txt_NewAddress.text,
                    'nickname':    self.ids.txt_NewNickname.text,
                    'password':    self.ids.txt_NewPassword.text,
                    'phoneNumber': self.ids.txt_NewPhoneNumber.text,
                    'username':    appData.current_username 
                }
            else:
                # 没改密码
                new_data = {
                    'address':     self.ids.txt_NewAddress.text,
                    'nickname':    self.ids.txt_NewNickname.text,
                    'password':    appData.current_password,
                    'phoneNumber': self.ids.txt_NewPhoneNumber.text,
                    'username':    appData.current_username 
                }

            user_ref.update(new_data)   #更新数据库

            # 更新appData
            appData.current_address = self.ids.txt_NewAddress.text
            appData.current_nickname = self.ids.txt_NewNickname.text
            appData.current_phoneNumber = self.ids.txt_NewPhoneNumber.text
            if self.ids.txt_OldPassword.text != '':
                appData.current_password = self.ids.txt_NewPassword.text

            dialog = MDDialog(
                text='successfully modified!',
                buttons=[]
            )
            dialog.open()
            Clock.schedule_once(lambda x: dialog.dismiss(), 2)
            Clock.schedule_once(lambda x: MDApp.get_running_app().switch_screen('navigator'), 2.5)
       
              



file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'update.kv'))


