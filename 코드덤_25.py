print('''
   (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/

''')


#name = ['홍길동', '철수', '영희']
##print(name)
##name.append('새영')
##print(name)
##name.remove('새영')
##print(name)

##
##import random
##import time
##print(" !! 커피 값 내기 !! 오늘은 누가 커피를 사게 될까요?")
##
##name = input("참가자들의 이름을 입력해주세요. 예) 철수 영희 >>>  ").split()
##
##print(f'총 {len(name)}명 참가하셨습니다.')
##print("오늘 선택된 사람은 ....")
##
##r= random.choice(name)
##time.sleep(2)
##
##print(f'{r}님 입니다.')






import random
import time

print('''

()  ()  ()
 ()  ()   ()
 ()  ()   ()
 ------------
 <           >
 |           |
 _____________





''')

print('커피값 내기!! 누가 커피값을 내게 될까요??')
name=input('참가자 들의 이름을 입력해주세요. 예) 철수 영희  >>>   ').split()

print(f'총{len(name)}명 참가하셨습니다.')
print('오늘 선택된 사람은...')
time.sleep(3)

bomb=random.choice(name)

print(f'{bomb}님 입니다.')




























