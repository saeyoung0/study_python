r=float(input("반지름을 입력해 주세요. \n"))

print(f"반지름 : {r} cm")
print(f"원 둘레 : {r*2*3.14} cm")
print(f"원 넓이 : {r*r*3.14} cm2")
print(f"원 넓이(거듭제곱 **) : {r**2*3.14}")

area = float(r**2*3.14)
circumference = r*2*3.14

print(f"원 넓이 : {round(area,2)}")

print(f"원 둘레 : {round(circumference)} cm")
