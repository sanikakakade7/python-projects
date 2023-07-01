# conditions for email
'''
    1. small letter a-z
    2.digits 0-9
    3. _ and . used only once before @
    4.use of @ only once
    5.the . that comes after @ should be at 2nd or 3rd position from behind
'''

import re   #re stands for regex module

email_conditions="^[a-z]+[a-z 0-9]+[\._]?[@]\w+[.]\w{2,3}$"

'''

 ^ means first character should be from a-z
 \._ means search ._ and ? returns 1 if they are present only once and 0 if they are not present at all 
 for multiple presence false condition
 [@]\w means search special character @ and special character is searched using \w
 then search special character . using \w at 2 and 3 position but from last so $ specifies check . at 2 and 3 position from last
 
'''

email=input("enter email")

if re.search(email_conditions,email):
    print('Right Email')
else:
    print('Wrong Email')