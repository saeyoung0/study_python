rock = '''

**
**

'''


scissor = '''

|   /
|  /
| /
|/

'''

paper = '''

*****
*****
*****


'''

import random

game_option =  [rock, scissor, paper]

com_choice = random.randint(0,1,2)

user_choice = int(input("0: 바위, 1: 가위, 2: 보 >>>   "))

print("나의 선택 : ")
print(game_option[user_choice])


print("컴퓨터의 선택 : ")
print(game_option[com_choice])

if com_choice == user_choice :
    print("비겼습니다.")
elif user_choice - com_choice == -1  or  (user_choice==2 and com_choice==0):
    print("사용자가 이겼습니다.")


else:
    print("졌습니다")

    
