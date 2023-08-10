door = '''

________
|       |       @@@@@@         $$$$$$
|   1   |       @  2 @         $  3 $ 
|_______|       @@@@@@         $$$$$$


'''


road = '''


_        |       _ 
\        |       /
/_  __   |  __  _\
  \/  \  |  /  \/
      /_ | _\
        \/


'''

import random

print('''
배팅 게임에 오신 것을 환영합니다.
한 레벨을 통과하실 때마다 배팅 금액의 2배를 상금으로 받으실 수 있습니다.
레벨 통과에 실패하시면 모든 배팅 금액을 읽게 됩니다. ''')
print("="*40)
print()

bet=int(input("배팅 금액을 입력하세요. 단위: $ >>>  "))
print(f"총 ${bet} 배팅하셨습니다.")


print(road)
winning_num = random.randint(1,3)
print(winning_num)

user_choice=int(input("3갈래의 길로 나뉘어 있습니다. 어느 길을 선택하시겠습니끼 1,2,3 >>>  "))

if user_choice == winning_num:
    print(f"축하합니다! 2배 획득!! 총 금액은 ${bet*2}가 되었습니다.")
    next_level=input("다음 단계로 이동하시겠습니까? 성공시 2배, 실패시 $0 y or n >>> ").lower()

    if next_level == "y" :
        print("다음 단계로 이동합니다.")
        print(door)

        winning_num ==random.randint(1,3)
        print(winning_num)

        user_choice=int(input("총 3개의 문이 있습니다. 하나를 선택해 주세요. 1,2,3 >>> "))

        if user_choice == winning_num:
            print(f"축하합니다! 2배 획득!! 총 금액은 ${bet*4}가 되었습니다.")
        else:
            print("door띠로리.. 모든 배팅 금액을 잃었습니다.")
            

    else:
        print(f"게임 종료. 총 금액은 ${bet*2}입니다. 축하드립니다.")


else:
    print("띠로리.. 모든 배팅 금액을 잃었습니다.")

    
         

