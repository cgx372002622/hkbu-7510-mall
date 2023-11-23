from app.utils.database import db_ref

class AppData:
    current_user = 'test'
    current_nickname = ''
    current_address = ''
    current_phoneNumber = ''

    def init_user(self, username):
        cur_users = db_ref.child('users').order_by_child('username').equal_to(username).limit_to_first(1).get() # 限制了返回的数组只有一个用户对象

        for k in cur_users.keys():
            cur_user = cur_users[k]
            self.current_user = cur_user.get('username')
            self.current_nickname = cur_user.get('nickname')
            self.current_address = cur_user.get('address')
            self.current_phoneNumber = cur_user.get('phoneNumber')

        print(self)

appData = AppData()

