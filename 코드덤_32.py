a=[0,1,2,3] #1차원 리스트
b=[['a','b'],['c','d']] #2차원 리스트

puzzle = [
    ["안녕을 다섯 번하면?","하이파이브"],
    ["아몬드가 죽으면?","다이아몬드"],
    ["언제나 한 짝 만 끼는 장갑은?","야구장갑"],
    ["이 세상을 모두 덮을 수 있는 것은?","눈꺼풀"]

    ]

score=0

for x,y in puzzle:
    print(x)
    user_input = input()

    if user_input == y:
        score+=1
        print(f"정답입니다.  현재 점수는 {score}점 입니다.")
    else:
        print(f"틀렸습니다. 정답은{y}입니다.")
    print()
        
print(f"총 {len(puzzle)}문제 중 {score}문제 맞혔습니다.")
