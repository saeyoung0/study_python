dict_eng={'apple':'사과',
         'peach':'복숭아',
         'mango':'망고',
         'spring':'봄',
         'summer':'여름',
         'autumn':'가을',
         'winter':'겨울'}





for i in dict_eng:
    user_input=input(f"{i}의 뜻은? >>>   ")

    if user_input == dict_eng[i]:
        print("정답입니다.")

    else:
        print(f"틀렸습니다. 정답은 {dict_eng[i]}입니다.")



























##
##for i in dict_eng:
##    
##
##    user_input=input(f"{i}의 뜻은? >>>")
##
##    if user_input == dict_eng[i]:
##        print(f"정답입니다.{i}")
##
##    else:
##        print(f"틀렸습니다. 정답은 {dict_eng[i]}입니다.")
##
