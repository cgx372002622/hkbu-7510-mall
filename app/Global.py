from app.utils.database import db_ref

class AppData:
    current_username = 'test'
    current_nickname = 'test'
    current_address = 'test'
    current_phoneNumber = 'test'
    current_userId = '-NjuSBGTMd745jwEf_Lq'
    current_password = 'test'
    passed_cart = [] # 从cart传给check的对象数组，对象：{'goods_id': '', 'count': '', 'key': ''}
    ready_passed_cart = [] # cart页面内部组件间交流使用

    def init_user(self, username):
        cur_users = db_ref.child('users').order_by_child('username').equal_to(username).limit_to_first(1).get() # 限制了返回的数组只有一个用户对象

        for k in cur_users.keys():
            cur_user = cur_users[k]
            self.current_username = cur_user.get('username')
            self.current_nickname = cur_user.get('nickname')
            self.current_address = cur_user.get('address')
            self.current_phoneNumber = cur_user.get('phoneNumber')
            self.current_password = cur_user.get('password')
            self.current_userId = k
            self.passed_cart = []
            self.ready_passed_cart = []

    def initialize(self):
        self.current_username = ''
        self.current_nickname = ''
        self.current_address = ''
        self.current_phoneNumber = ''
        self.current_password = ''
        self.current_userId = ''
        self.passed_cart = []
        self.ready_passed_cart = []


appData = AppData()

