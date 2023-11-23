from app.utils.database import db_ref

class AppData:
    current_username = 'test'
    current_nickname = ''
    current_address = ''
    current_phoneNumber = ''
    current_userId = '-NjuSBGTMd745jwEf_Lq'

    def init_user(self, username):
        cur_users = db_ref.child('users').order_by_child('username').equal_to(username).limit_to_first(1).get() # 限制了返回的数组只有一个用户对象

        for k in cur_users.keys():
            cur_user = cur_users[k]
            self.current_username = cur_user.get('username')
            self.current_nickname = cur_user.get('nickname')
            self.current_address = cur_user.get('address')
            self.current_phoneNumber = cur_user.get('phoneNumber')
            self.current_userId = k

        print(self)

appData = AppData()

