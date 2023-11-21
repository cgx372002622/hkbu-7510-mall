import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from app.utils.database import db_ref




class Register(Screen):
    # def register(self):
    #     dialog = MDDialog(
    #         title = 'Successful registration',
    #         text = 'This is your personal information',
    #         buttons = [
    #             MDRaisedButton(
    #                 text = 'Complete Registration',
    #                 on_press = lambda x: dialog.dismiss(),
    #                 on_release = lambda x: MDApp.get_running_app().switch_screen("login")
    #                 ),
    #         ]
    #     )
    #     dialog.open()

    def cancel(self):
        self.ids.text_username.text = ''
        self.ids.text_password.ids.text_field.text = ''
        self.ids.text_nickname.text = ''
        self.ids.text_phoneNumber.text = ''
        self.ids.text_address.text = ''

    def submit_data(self):
        username = self.ids.text_username.text
        password = self.ids.text_password.ids.text_field.text
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
        query1_result = users_ref.order_by_child('username').get()

        username_exists = False   #判断username是否已经存在

        if query1_result is not None:
            for result in query1_result.values():
                query = result['username']
                if username == '' or password == '' or nickname == '' or phoneNumber == '' or address == '':
                    dialog1 = MDDialog(
                        title = 'Warning',
                        text = 'Anyone of the text field is empty!',
                        buttons = [
                            MDRaisedButton(
                                text = 'Return',
                                on_press = lambda x: dialog1.dismiss(),
                            )
                        ]
                    )
                    dialog1.open()
                    break

                elif query == username:
                    username_exists = True
                    break

        if username_exists:

                    dialog2 = MDDialog(
                        title = 'Warning',
                        text = 'Username already exists',
                        buttons = [
                            MDRaisedButton(
                                text = 'Return',
                                on_press = lambda x: dialog2.dismiss(),
                            )
                        ]
                    )
                    dialog2.open()

                    # dialog3 = MDDialog(
                    #     title = 'Warning',
                    #     text = 'Nickname already exists',
                    #     buttons = [
                    #         MDRaisedButton(
                    #             text = 'Return',
                    #             on_press = lambda x: dialog3.dismiss(),
                    #         )
                    #     ]
                    # )
                    # dialog3.open()
        
        else:
            users_ref = db_ref.child('users')
            users_ref.push(data)

            dialog3 = MDDialog(
                title = 'Congraduations!',
                text = 'Registion successful!',
                buttons = [
                    MDRaisedButton(
                        text = 'Finish',
                        on_press = lambda x: dialog3.dismiss(),
                        on_release = lambda x:MDApp.get_running_app().switch_screen("login")
                    )
                ]
            )
            dialog3.open()

            self.ids.text_nickname.text = ''
            self.ids.text_password.ids.text_field.text = ''
            self.ids.text_nickname.text = ''
            self.ids.text_phoneNumber.text = ''
            self.ids.text_address.text = ''


file_path = os.path.dirname(__file__)

Builder.load_file(os.path.join(file_path,'register.kv'))

