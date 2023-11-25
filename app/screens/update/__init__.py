import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from app.utils.database import db_ref
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.core.window import Window
from app.Global import appData
from firebase_admin import db

class Update(Screen):
    username=appData.current_username  
    password=appData.current_password
    # appData = 'appData'
    # def get_current_username(self,password1):
    #     appData.current_password = password1
        
    def set_username(self, cur_user):
        self.username = cur_user

    def cancel(self):   #清理全部文本
        self.ids.txt_OldPassword.text = ''
        self.ids.txt_NewPassword.text = ''
        self.ids.txt_ConfirmNewPassword.text = ''
        self.ids.txt_NewNickname.text = ''
        self.ids.txt_NewPhoneNumber.text = ''
        self.ids.txt_NewAddress.text = ''
    
    def OldPassword_vertify(self):   #判断输入的文本是否有问题（密码不一致或者是否有空的），没问题就上传更新用户数据
        self.Oldpassword = self.ids.txt_OldPassword.text

        if  (self.Oldpassword == '' or self.ids.txt_NewPassword.text == '' or self.ids.txt_ConfirmNewPassword.text == '' or self.ids.txt_NewNickname.text == '' or self.ids.txt_NewPhoneNumber.text == '' or self.ids.txt_NewAddress.text == '' ):
            dialog2 = MDDialog(
                title='Retry',
                text='One or more the messages is empty!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog2.dismiss(),
                    )
                ]
            )
            dialog2.open()
            return
        elif self.Oldpassword != appData.current_password:
                
            dialog1 = MDDialog(
                title='Retry',
                text='Please enter corret old password!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog1.dismiss(),
                    )
                ]
            )
            dialog1.open()
            return
        elif self.ids.txt_NewPassword.text   !=   self.ids.txt_ConfirmNewPassword.text :
            
            dialog3 = MDDialog(
                title='Retry',
                text='The new password is different from the confirmed password!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog3.dismiss(),
                    )
                ]
            )
            dialog3.open()
            return
        
        else : # 上传到firebase更新用户数据，更新到Gobal和Update的类属性
        
            users_ref = db.reference('users')
            query = users_ref.order_by_child('username').equal_to(appData.current_username)
            results = query.get()

            user_id = next(iter(results.keys()))
            user_ref = users_ref.child(user_id)
            new_data = {
                    'address':     self.ids.txt_NewAddress.text,
                    'nickname':    self.ids.txt_NewNickname.text,
                    'password':    self.ids.txt_NewPassword.text,
                    'phoneNumber': self.ids.txt_NewPhoneNumber.text,
                    'username':    appData.current_username 
                    # 更新的数据
                }
            user_ref.update(new_data)   #更新数据库
           
            appData.current_nickname = self.ids.txt_NewNickname.text
            appData.current_address = self.ids.txt_NewNickname.text
            appData.current_phoneNumber = self.ids.txt_NewPhoneNumber.text
            appData.current_password = self.ids.txt_NewPassword.text         
            self.password=self.ids.txt_NewPassword.text  #更新Update的类属性和Gobal的用户属性，方便用户更多次修改密码
            print("用户数据已成功更新")
            print("New Address: "+appData.current_address)
            print("New Nickname: "+appData.current_nickname)
            print("New Password: "+appData.current_password)
            print("New Phone Number: "+appData.current_phoneNumber)
            print("Username: "+appData.current_username)
            dialog3 = MDDialog(
                title='Succeed',
                text='The personal information was successfully modified!',
                buttons=[
                    MDRaisedButton(
                        text='OK',
                        on_press=lambda x: dialog3.dismiss(),
                    )
                ]
            )
            dialog3.open()
            return
       
              



file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'update.kv'))


