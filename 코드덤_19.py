print("Welcome To")
print("!!! MAth Quiz !!!")
print('''

   111
     1   
     1
     1   
     1
  111111      


''')

import random
import time

playing = True

score=0
count=0

start_time=time.time()
while playing:

    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,10)

    answer=a*b-c
    my=int(input(f"{a}x{b}-{c}=    "))
    count +=1
    


    if answer == my:
        score +=1
        print(f"정답입니다. 현재 점수는 {score}입니다.")
        
    else:
        playing=False
        print(f"틀렸습니다. 정답은 {answer} 입니다.")

end_time=time.time()
my_time=round(end_time-start_time,1)
print(f"총 {count}문제를 {my_time}초만에 해결하셨습니다.")
print(f"Math Quiz가 종료되었습니다. 총 {score}번 만에 맞추셨습니다.")
