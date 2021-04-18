# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:39:32 2021
I conducted Hacking the Fender project with Python. 
I used my knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. 
I worked with CSV files and other text files in this exploration of the strength of Python file programming.
'passwords.csv' file is essential to conduct this project which contains the data of compromised users. 
Assume the situation, there is a person called The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including my own. 
My mission, should I choose to accept it, is threefold. I must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble the secret data. 
The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.

@author: Sarp
"""
import csv
import json
compromised_users=[]
with open('passwords.csv') as password_file:
  password_csv=csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])
with open('compromised_users.txt','w') as compromised_user_file:
  for comprimised_user in compromised_users:
    compromised_user_file.write(comprimised_user)
with open('boss_message.json','w') as boss_message:
  boss_message_dict={'recipient':'The Boss', 'message':'Mission Success'}
  json.dump(boss_message_dict, boss_message)
with open('new_passwords.csv','w') as new_passwords_obj:
  slash_null_sig="""            
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""
  new_passwords_obj.write(slash_null_sig)
