import urllib.request

import pyrebase
firebaseConfig = {
    'apiKey': "AIzaSyAP1VhmmN7TkyxiWDldOJ7_6EKdNMHHmus",
    'authDomain': "fir-project-c8247.firebaseapp.com",
    'databaseURL': "https://fir-project-c8247-default-rtdb.firebaseio.com/",
    'projectId': "fir-project-c8247",
    'storageBucket': "fir-project-c8247.appspot.com",
    'messagingSenderId': "620649024781",
    'appId': "1:620649024781:web:19c0f445d4d2db9211b444",
    'measurementId': "G-F36ZV5LXST"
  };

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# auth = firebase.auth()

# storage = firebase.storage()

# Authentification

# Sign In

# email = input('Enter Email: ')
#
# password = input('Enter Password: ')
#
# try:
#     auth.sign_in_with_email_and_password(email, password)
#     print('Successfully signed in')
# except:
#     print('Invalid user or password. Plase, Try Again')

# Sign Up

# email = input('Enter Email: ')
#
# password = input('Enter Password: ')
#
# password_conf = input('Confirm Password: ')
#
# if password == password_conf:
#     try:
#         auth.create_user_with_email_and_password(email, password)
#         print('Success!!!')
#     except:
#         print('Email already exist')


# Storage

# upload
# filename = input('Enter file for upload: ')
# cloudfilename = input('Enter filename on the cloud: ')
# storage.child(cloudfilename).put(filename)

#download
# cloudfilename = input('Enter file for download: ')
# storage.child("google.txt").download("", "downloaded.txt")

#reading file
# cloudfilename = input('Enter filename for read: ')
# url = storage.child(cloudfilename).get_url(None)
# f = urllib.request.urlopen(url).read()
# print(f)

# Database

#create
data = {'name': "John Smith", 'age': 40, 'employed': True, 'address': "Nyu York"}
# db.push(data)
# db.child("people").child("person").push(data)
# db.child("people").child("person").child("myid").set(data)

#update
# db.child("people").child("person").child("myid").update({'name': "Jane"})
# db.child("people").child("person").child("myid").update({'names': "Jane"})
persons = db.child("people").child("person").get()
for person in persons.each():
    # print(person.key())
    # print(person.val())
    if person.val()['name'] == 'John Smith':
        db.child("people").child("person").child(person.key()).update({'name': "Jane"})

