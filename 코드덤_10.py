print("="*20)
print("체질량 지수 BMI를 확인해 보세요!")
print("="*20)
print()


height = float(input("키를 입력하세요(단위: 미터) : "))
weight = float(input("몸무게를 입력하세요 : "))


bmi = round(weight / height**2,1)
print(bmi)
bmi_icon = "ㅁ"

if bmi < 18.5:
    print(bmi_icon)
    print("저체중 입니다.")

elif 18.5 <= bmi < 25:
    
    print(bmi_icon*2)
    print("정상 입니다.")

elif 25<= bmi <30:
    print(bmi_icon*3)
    print("경도 비만 입니다.")

else:
    print(bmi_icon*4)
    print("과체중 입니다. 당장 다욧 하세요!")
 
