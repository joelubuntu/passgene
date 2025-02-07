import datetime , random , os , sys , platform
try:
	from cryptography.fernet import Fernet
except:
	if platform.system() == 'Windows':
		os.system("pip install cryptography")
	elif platform.system() == 'Linux':
		os.system("pip3 install cryptography")
		
def pass_gen():
	a = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	b = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	c = random.choice([':','!','@','#','$','%','^','&','*','(',')','_','+','|',';','.','`','<','>','?','~'])
	d = random.choice(['1','2','3','4','5','6','7','8','9','0'])
	e = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	f = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	g = random.choice([':','!','@','#','$','%','^','&','*','(',')','_','+','|',';','.','`','<','>','?','~'])
	h = random.choice(['1','2','3','4','5','6','7','8','9','0'])
	i = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	j = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	k = random.choice([':','!','@','#','$','%','^','&','*','(',')','_','+','|',';','.','`','<','>','?','~'])
	l = random.choice(['1','2','3','4','5','6','7','8','9','0'])
	m = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	n = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	o = random.choice([':','!','@','#','$','%','^','&','*','(',')','_','+','|',';','.','`','<','>','?','~'])
	password = ''
	for i in range(15):
		unit = random.choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o])
		password += str(unit)
	print("\nYour random 10 digit password is: " + password)
	user_input = input("\nWould you like to save your password? \n Press y for YES and n for NO: ")
	if user_input.lower() == ('y'):
		account = input("\nThis password is for which site / app : ")
		username = input("username of " + account + ": " )
		appending_txt = ("\n\n\n" + account + "\n" + "username : " + username + "\nyour password of " + account + " is: " + password)
		decrypt(appending_txt)
	else:
		print("Okay as you wish!")

def add():
	account = input("\nThis account is of: ")
	username = input("Enter your account username: ")
	passwd = input ("Enter your password: ")
	appending_txt = ("\n\n\n" + account + "\n" + "username : " + username + "\nyour password of " + account + " is: " + passwd)
	decrypt(appending_txt)

def view_pass():
	with open(".en_data.txt","rb") as en_data:
		data = en_data.read()
	with open(".key.key","rb") as key:
		Key = key.read()
	f = Fernet(Key)
	de_data = f.decrypt(data)
	with open(".de_data.txt","wb") as de_file_data:
		de_file_data.write(de_data)
	de_file_data.close()
	key.close()
	en_data.close()
	view = open('.de_data.txt','r')
	print(view.read())
	view.close()
	os.remove(".de_data.txt")

def welcome():
	name = os.getlogin()
	time = datetime.datetime.now().hour
	if time <= 12 and time >= 5:
		print('Good Morning')
	elif time <= 17 and time >=12:
		print("Good Afternoon")
	elif time <= 23 and time >= 17:
		print("Good Evening")
	print(name)

def encrypt():
	with open('.de_data.txt','rb') as file_data:
		data = file_data.read()
	with open('.key.key','rb') as key:
		Key = key.read()
	f = Fernet(Key)
	en_data = f.encrypt(data)
	with open('.en_data.txt','wb') as en_file_data:
		en_file_data.write(en_data)
	en_file_data.close()
	key.close()
	file_data.close()
	os.remove('.de_data.txt')
	print('Done!')

def decrypt(appending_txt):
	with open(".en_data.txt","rb") as en_data:
		data = en_data.read()
	with open(".key.key","rb") as key:
		Key = key.read()
	f = Fernet(Key)
	de_data = f.decrypt(data)
	with open(".de_data.txt","wb") as de_file_data:
		de_file_data.write(de_data)
	new_de = open('.de_data.txt','a')
	new_de.write(appending_txt)
	new_de.close()
	key.close()
	en_data.close()
	de_file_data.close()
	os.remove('.en_data.txt')
	encrypt()

def dev_decrypt():
	with open(".en_data.txt","rb") as en_data:
		data = en_data.read()
	with open(".key.key","rb") as key:
		Key = key.read()
	f = Fernet(Key)
	de_data = f.decrypt(data)
	with open(".de_data.txt","wb") as de_file_data:
		de_file_data.write(de_data)
	en_data.close()
	key.close()
	de_file_data.close()

def reset():
	os.remove(".key.key")
	os.remove(".en_data.txt")
	os.remove(".master_key.txt")
	exit = True

def main_menu():
	with open('.master_key.txt','rb') as master_key:
		master_pass = master_key.read()
	user_key = input("\n Enter your master password: ")
	with open('.key.key' , 'rb') as key:
		Key = key.read()
	f = Fernet(Key)
	passwd = f.decrypt(master_pass)
	if passwd == user_key.encode():
		key.close()
		master_key.close()
		print("Access Granted! \n")
		print('+------------------------------------------------------------------------------------------------+')
		print("|gen pass - it genrates new password of 10 digits.                                               |")
		print("|view pass - it prints saved password if file is not renamed or modified.                        |")
		print("|add - through this feature you can add you custom password in password file.                    |")
		print("|reset - it format saved password database                                                       |")
		print('+------------------------------------------------------------------------------------------------+')
		global exit , reset_B
		exit,reset_B  = False , False
		while exit == False and reset_B == False:
			user_input = str(input("Enter your command: "))
			if user_input.lower() == "exit" or user_input.lower() == "quit":
				exit = True
			elif user_input.lower() == ("gen pass"):
				pass_gen()
			elif user_input.lower() == ("view pass"):
				view_pass()
			elif user_input.lower() == ("add"):
				add()
			elif user_input.lower() == ("dev_decrypt"):
				dev_decrypt()
			elif user_input.lower() == ("encrypt"):
				encrypt()
			elif user_input.lower() == ("settings change master key"):
				master_change()
			elif user_input.lower() == "clear" or user_input.lower() == "cls":
				if platform.system() == 'Windows':
					os.system("cls")
				elif sys.platform == ("linux") or sys.platform == ("linux2"):
					os.system("clear")
			elif user_input.lower() == ("reset"):
				verify = input("Type YES to proceed reset operation: ")
				if verify == ("YES"):
					print('Password database has been deleted')
					reset_B = True
					reset()
				else:
					print("reset operation STOPED!")
			else:
				print('\nEnter valid command.\n')
	else:
		print("Try Again!")
		main_menu()

def init():
	Key = Fernet.generate_key()
	f = Fernet(Key)
	master_password = input("Set your master password: ").encode()
	with open('.key.key' , 'wb') as key:
		key.write(Key)
	en_master = f.encrypt(master_password)
	with open('.master_key.txt','wb') as master_key:
		master_key.write(en_master)
	en_data = open(".de_data.txt","w")
	en_data.write("This is Password file!")
	en_data.close()
	key.close()
	master_key.close()
	encrypt()
	if platform.system() == 'Windows':
		os.system("attrib +h .master_key.txt")
		os.system("attrib +h .en_data.txt")
		os.system("attrib +h .key.key")
	print('setup completed!')
	main_menu()

def master_change():
	os.remove(".master_key.txt")
	master_password = input("Set your new master password: ").encode()
	with open('.key.key','rb') as key:
		Key = key.read()
	f = Fernet(Key)
	en_pass = f.encrypt(master_password)
	with open('.master_key.txt','wb') as master_key:
		master_key.write(en_pass)
	master_key.close()
	key.close()
	print("password changed! ")
	main_menu()

#welcome()

try:
	key_open = open('.key.key','r')
	key_open.close()
except:
	init()

if platform.system() == 'Windows':
	os.system("attrib +h .en_data.txt")
	os.system("attrib +h .key.key")
	os.system("attrib +h .master_key.txt")

try:
	with open('.master_key.txt','rb') as master_key:
		master_pass = master_key.read()
	user_key = str(sys.argv[1])
	with open('.key.key' , 'rb') as key:
		Key = key.read()
	f = Fernet(Key)
	passwd = f.decrypt(master_pass)
	if passwd == user_key.encode():
		key.close()
		master_key.close()
		print("Access Granted! \n")
		if platform.system() == 'Windows':
			os.system("powershell;Remove-Item (Get-PSReadlineOption).HistorySavePath")
		else:
			os.system("history -c")
		if sys.argv[2].lower() == ("gen"):
			pass_gen()
		elif sys.argv[2].lower() == ("view"):
				view_pass()
		elif sys.argv[2].lower() == ("add"):
			add()
		elif sys.argv[2].lower() == ("dev_decrypt"):
			dev_decrypt()
		elif sys.argv[2].lower() == ("encrypt"):
			encrypt()
		elif sys.argv[2].lower() == ("settings change master key"):
			master_change()
		elif sys.argv[2].lower() == "clear" or sys.argv[2].lower() == "cls":
			if platform.system() == 'Windows':
				os.system("cls")
			elif platform.system() == 'Linux':
				os.system("clear")
		elif sys.argv[2].lower() == ("reset"):
			verify = input("Type YES to proceed reset operation: ")
			if verify == ("YES"):
				print('Password database has been deleted')
				reset_B = True
				reset()
			else:
				print("reset operation STOPED!")
		else:
			print('\nEnter valid command.\n')
except:
	main_menu()

#last updated 25 APRIL 2023
