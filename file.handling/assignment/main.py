import os
import getpass

if not os.path.exists('record.txt'):
    open('record.txt','w').close()


def register():
    username=input("Enter username: ")
    if username in open('record.txt').read():
        print('Username exists')
        exit()
    password=getpass.getpass("Enter password: ")
    confirm_pw=getpass.getpass("Confirm password: ")
    if password!=confirm_pw:
        print('Password does not match')
        exit()

    file=open('record.txt','a')
    file.write(usename)
    file.write('')

        print('Registration success')
        exit()


def login():
    username=input("enter username: ")




    #     increment+=1
    # if login_success==True:


#s.n name  password
#1.  ram    ram