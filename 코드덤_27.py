print('''

  _
 {_}
 |(|
 |=|
/   \
|.--|
||  |
||  |    .    ' .
|'--|  '     \~~~/
'-=-' \~~~/   \_/
       \_/     Y
        Y     _|_
jgs    _|_

''')

print("== 새영 주스 카페 관리자 모드 ==")

flavor = ["사과", "당근", "망고"]

#for i in range(3):
 #   print(f"{flavor[i]} 주스")


for i in flavor:
    print(f"{i} 주스")

user_input=0
while user_input != 5:

    print("""
    ==관리자 모드 ==
    1. 메뉴보기
    2. 신메뉴 추가하기
    3. 메뉴 삭제하기
    4. 메뉴 이름 바꾸기
    5. 관리지 모드 종료하기
    ====================
    """)

    user_input = input("원하는 기능을 선택하세요. >>> ")
    if user_input =='1':
        print("==메뉴==")
        for i in flavor:
            print(f"{i} 주스")

    elif user_input =='2':
        new_flavor = input("추가할 메뉴 이름을 입력해 주세요 >>> ")
        flavor.append(new_flavor)


    elif user_input =='3':
        remove_flavor = input("삭제할 메뉴 이름을 입력해 주세요 >>> ")
        flavor.remove(remove_flavor)

    elif user_input =='4':
        for i in range(len(flavor)):
            print(f"{i}.{flavor[i]}")

        index = int(input("몇 번째 메뉴를 변경하시겠습니까?"))
        new_name = input("변경할 이름을 입력해 주세요")

        print(f"{flaver[i]} 메뉴를 {new_name}으로 변경합니다.")
        flavor[index] = new_name

        
        
