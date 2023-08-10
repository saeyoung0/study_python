c_art = '''
     )  (
     (   ) )
      ) ( (
 mrf_______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '--------

'''
print(c_art)
print(''' 코드덤 커피 자판기
            - 메    뉴 -
        1 : 아메리카노 1,800원
        2 : 카페라떼   2,700원
        3 : 핫초코     2,300원


''')
print("="*40)




coffee_price = 0
order=int(input("커피 종류를 선택하세요. 번호 입력>>>  "))
total_price = 0


if 1 <= order <= 3:
        
    if order == 1:
        coffee_price = 1800
    elif order ==2:
        coffee_price = 2700
    elif order ==3:
        coffee_price = 2300

            
    cups = int(input("몇 잔을 드릴까요? ??? "))
    total_price=coffee_price*cups
    print(total_price)
        


    received = int(input(f"총 금액은 {total_price}원 입니다. 돈을 투입해 주세요 >>>  "))

    if received >= total_price:
        change = received - total_price
        print(f"{received}원 받았습니다. 거스름돈은 {change}원 입니다.")

        change_1000 = change // 1000
        reamin_1000 = change % 1000
        change_500 = reamin_1000 // 500
        remain_500 = remain_1000 % 500
        change_100 = reamin_500 // 100

        print(f"1000원짜리 {change_1000}개, 500원짜리 {change_500}개, 100원짜리 {change_100}개 필요합니다.")

    elif received < total_price:
        print(f"{received}원 받았습니다.  {total_price-received}원 모자랍니다.")

else:
    print("잘못된 주문입니다. 다시 확인해주세요")
