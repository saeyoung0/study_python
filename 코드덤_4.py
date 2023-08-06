
#name = input("이름을 적어주세요.")
#print(name+"님 안녕하세요")


print("사과 1개 : 500원")
count = int(input("사과 몇개를 드릴까요?")) #integer 정수
#print("총 금액은 ",count*500,"원 입니다.")  # + -> 문자와 문자끼리 합할때

#f-string 3.6ver 이상
print(f"총 금액은 {500*count}원 입니다.")
