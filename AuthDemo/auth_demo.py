import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()
#firebase configuration
firebaseConfig = {
    'apiKey': os.getenv("apiKey"),
    'authDomain': os.getenv("authDomain"),
    'projectId': os.getenv("projectId"),
    'databaseURL': os.getenv("databaseURL"),
    'storageBucket': os.getenv("StorageBucket"),
    'messagingSenderId': os.getenv("messagingSenderId"),
    'appId': os.getenv("appId"),
    'measurementId': os.getenv("measurementId")
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

#signup
def signup():
    print("Signup \n")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        user=auth.create_user_with_email_and_password(email, password)
        print("Successfully created account")
        ask=input("Do you want to login [y/n]: ")
        if ask.lower() == 'y':
            login()
    except Exception as e:
        print("Error during account creation:\n", str(e))
    
# Login
def login():
    print("Log in \n")
    email=input("Enter email: ")
    password=input("Enter password: ")
    
    try:
        login=auth.sign_in_with_email_and_password(email, password)
        print("Succesfully logged in")
        print(auth.get_account_info(login['idToken']))
    except Exception as e:
        print("Error occured : \n",str(e))
        print()
        ask=input("Do you want to change password [y/n]: ")
        if ask.lower() == 'y':
            forgotPassword()
    
# Forgot Password
def forgotPassword():
    email = input("Enter your email to reset the password: ")

    try:
        auth.send_password_reset_email(email)
        print("Password reset email sent successfully")
    except Exception as e:
        print(str(e))
        
# input 
ans=input("Are you a new user [y/n]: ")
if ans.lower() == 'y':
    signup()
elif ans.lower() == 'n':
    login()
else:
    print("Invalid response")
    
