import random
import os
import datetime
from cryptography.fernet import Fernet
def welcome():
    user_name = os.getlogin()
    time = datetime.datetime.now().hour
    if time <= 12 and time >= 5:
        print('Good morning,')
    elif time <= 17 and time >= 12:
        print('Good afternoon,')
    elif time <= 23 and time >= 17:
        print('Good evening,')
    return user_name
def password_generator():
    print('Welcome to Password generator :)') 
    a = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    b = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    c = random.choice([':','!','@','#','$','%','^','&','*','(',')','_','+','|',';','.','`','<','>','?','~'])
    d = random.choice(['1','2','3','4','5','6','7','8','9','0'])
    e = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    f = random.choice(['1','2','3','4','5','6','7','8','9','0'])
    g = random.choice([':','!','@','#','$','%','^','&','*','(',')','_','+','|',';','.','`','<','>','?','~'])
    h = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    i = random.choice(['no','hm','lo','py','gg','op','hi'])
    j = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    print("Your random 10 digit password is: \n")
    password = ( a + b + c + d + e + f + g + h + i + j)
    print (password)
    print("\n")
    for i in range(3):
        print("would you like to save your password ? ")
        z = input("Press y for yes , n for no , q for quit: ")
        z.lower()
        if z == ("q"):
            break
        if z == ("y"):
            user_name = input("Enter your account username: ")
            account = input('This account is of:  ')
            x = input("have you ever saved a file through this script\nPress y for yes and n for no: ")
            if x == ('y'):
                password_file = open("password.txt" , "a")
                password_file.write("\n\n")
                password_file.write(account)
                password_file.write("\n")
                password_file.write("your username is " + user_name)
                password_file.write("\n")
                password_file.write("your password of " + account + " is " + password)
                password_file.close()
                print("Your password file is saved :3")
            elif x == ('n'):
                password_file = open("password.txt" , "w")
                password_file.write(account)
                password_file.write("\n\n")
                password_file.write("your username is " + user_name)
                password_file.write("\n")
                password_file.write("your password of " + account + " is " +password)
                password_file.close()
                print("Your password file is saved :3")
            else:
                print("invalid input")
        else:
            print("As you wish \n have a nice day")
def add():
    account = input("This account is of: ")
    user_name = input("Enter your account username: ")
    password = input ("Enter your password: ")
    password_file = open("password.txt" , "a")
    password_file.write("\n\n")
    password_file.write(account)
    password_file.write("\n")
    password_file.write("your username is" + user_name)
    password_file.write("\n")
    password_file.write("your password of " + account + "is" + password + "\n")
    password_file.close()
    print("Password was saved :3")
def pass_view():
    try:
        password_file = open("password.txt" , "r")
        print("Your saved passwords are: \n")
        print(password_file.read())
        password_file.close()
    except:
        print("file unavailable!")
def encrypt():
    try:
        Key = Fernet.generate_key()
        f = Fernet(Key)
        with open('key.key','wb') as key:
            key.write(Key)
        with open('password.txt','rb') as passwords:
            plain_txt = passwords.read()
        en_txt = f.encrypt(plain_txt)
        with open('en_password.txt','wb') as en_pass:
            en_pass.write(en_txt)
        print('Encryption done!')
    except:
        print('failed encryption!')
def decrypt():
    try:
        with open('key.key','rb') as key:
            Key = key.read()
        f = Fernet(Key)
        with open('en_password.txt','rb') as en_pass:
            en_txt = en_pass.read()
        de = f.decrypt(en_txt)
        with open('de_password.txt','wb') as de_pass:
            de_pass.write(de)
        print('Decryption done!')
    except:
        print('failed decryption')
def help():
    print("gen pass - it genrates new password of 10 digits.")
    print("view pass - it prints saved password if file is not renamed or modified.")
    print("add - through this feature you can add you custom password in password file. ")
    print("encrypt - it encrypt password file")
    print("decrypt - it decrypt password file")
    print("thats all , I'm noob in this ;-;")
print(welcome())
print('Type help for help.')
user_cmd = input("Enter your command here: ")
if (user_cmd.lower()) == ("gen pass"):
    password_generator()
elif (user_cmd.lower()) == ("help"):
    help()
elif (user_cmd.lower())  == ("view pass"):
    pass_view()
elif (user_cmd.lower())  == ("add"):
    add()
elif user_cmd.lower() == ("encrypt"):
    encrypt()
elif user_cmd.lower() == ("decrypt"):
    decrypt()
else:
    print("Invalid input")
# coded by !     Mr.JoE  
# created on 22 OCT 2020
# updated on 6 JAN 2021
# no copyright :3
