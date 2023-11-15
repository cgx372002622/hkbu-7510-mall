import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()

import firebase_admin
from firebase_admin import db
cred_obj = firebase_admin.credentials.Certificate('app/resources/serviceAccountKey.json')
firebase_admin.initialize_app(cred_obj, {
    'databaseURL':'https://comp7510-mall-default-rtdb.firebaseio.com/',
    'storageBucket': 'comp7510-mall.appspot.com/'
})

db_ref = db.reference('/')