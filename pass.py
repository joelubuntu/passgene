import random
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
    password = ( a + b + c + d + e + f + g + i + j)
    print (password)
    print("\n")
    for i in range(1):
        print("would you like to save your password ? ")
        z = input("Press y for yes , n for no , q for quit: ")
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
                password_file.write("\n")
                password_file.write("your username is " + user_name)
                password_file.write("\n")
                password_file.write("your password of " + account + " is " +password)
                password_file.close()
                print("Your password file is saved :3")
            else:
                print("invalid input")
        else:
            print("As you wish \n have a nice day")
def pass_view():
    try:
        password_file = open("password.txt" , "r")
        print("Your saved passwords are: \n")
        print(password_file.read())
        password_file.close()
    except:
        print("file unavailable!")
def help():
    print("gen_pass - it genrates new password of 10 digits")
    print("view_pass - it prints saved password if file is not renamed or modified")
    print("thats all , I'm noob in this ;-;")

print('Type help for help.')
user_cmd = input("Enter your command here: ")
if user_cmd == ("gen_pass"):
    password_generator()
elif user_cmd == ("help"):
    help()
elif user_cmd  == ("view_pass"):
    pass_view()
else:
    print("Invalid input")
# coded by !     Mr.JoE  
# created on 22 OCTOBER 2020
# updated on 22 OCTOBER 2020
# no copyright :3
