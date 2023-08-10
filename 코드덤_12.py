art_100= '''

       .---.
      /     \
      \.@-@./
      /`\_/`\
     //  _  \\
    | \     )|_
   /`\_`>  <_/ \
jgs\__/'---'\__/




'''



print(art_100)
print('''100세 시대 !!
100세. 나는 어떤 모습일까요?
상상이 되시나요?
''')

age = int(input("현재의 나이를 입력하세요 >>> "))
rest_of_life = 100 - age
print(age)
print("\n여기까지 달려오셨어요 !!")
#print("*"*age+"_"*rest_of_life)

print("*"*age, end='') #print("^"*age, end='#')
print("_"*rest_of_life)


print(f"일년에 한번씩 새로운 취미 만들기에 도전한다면 {rest_of_life}개의 새로운 도전")
print(f"한달에 한번씩 여행 간다면 {rest_of_life*12 :,} 곳에서의 추억")
print(f"일주일에 책 한권씩 읽는다면 {rest_of_life*52 :,} 권의 책")
print(f"하루에 1개의 영어 단어를 외운다면 {rest_of_life*365:,}개의 단어")
    

