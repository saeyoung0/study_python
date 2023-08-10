import random

picture='''


@@@@@@@@@
@@     @@
@@  ?  @@
@@     @@
@@@@@@@@@


'''

print(picture)

print("카드 뒷면에 1~20사이의 수가 있습니다. 어떤 숫자가 숨겨져 있을까요?")


card_num=random.randint(1,20)
guess_num=0
attempt=0

while card_num != guess_num :
    guess_num=int(input("다시 맞춰보세요 >>>   "))
    attempt+=1
    if card_num > guess_num:
        print("더 큰 수 입니다.")

    elif card_num < guess_num:
        print("더 작은 수 입니다.")
    print()
print(f"정답! 총 {attempt}번 만에 맞췄습니다.")







'''
card_num=random.randint(1,20)
user_guess = 0
attempt=0

while card_num != user_guess :
    user_guess=int(input("카드 뒷면의 수를 추측해 보세요~! >>>   "))
    attempt+=1
    if card_num > user_guess :
        print("더 큰 수 입니다.")
    elif card_num < user_guess :
        print("더 작은 수 입니다.")
    print()
print(f"정답 입니다.총 {attempt}번 만에 맞추셨습니다.")


'''
