from flask import Flask
import pyrebase

config = {
    "apiKey": "AIzaSyAtrr9CK-DDzGyTkYuw1QVLYujPChe6QDQ",
    "authDomain": "helloworld-950b1.firebaseapp.com",
    "databaseURL": "https://helloworld-950b1-default-rtdb.firebaseio.com",
    "projectId": "helloworld-950b1",
    "storageBucket": "helloworld-950b1.appspot.com",
    "messagingSenderId": "399897497806",
    "appId": "1:399897497806:web:889379fd3a8e2b79d6009f",
    "measurementId": "G-RV1Y1J8M24"
  }
firebase=pyrebase.initialize_app(config)
db=firebase.database()
app=Flask(__name__)
@app.route('/palani',methods=['GET'])
def mains():
    a=db.child("text").child("name").get()
    value=a.val()
    return {
        'text':value
    }
