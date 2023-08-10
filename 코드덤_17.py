lock='''

                                                         ,jf
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"

'''


wrong_pwd='''

                                                        ,jf
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"

잘못된 비밀번호 입니다.

'''

unlock='''

     |""-..._____
     '-.____    _````"""""'`|
         \  ``` ``"---... _ |
         |              /  /#\
         }--..______..-{   ###
        }}}}} _   _ {{{{{
        }}}}  6   6  {{{{
       {{{{{    ^    }}}}}
      {{{{{{\  -=-  /}}}}}}
      {{{{{{{;.___.;}}}}}}}
       {{{{{{{)   (}}}}}}}'
        `""'"':   :'"'"'`
after/jgs      `@`

Congratulations~!!
'''



print(lock)

pwd="a1234!"


user_input=input("비밀번호를 입력하세요. >>>   ")
while user_input != pwd:
    print(wrong_pwd)
    user_input=input("잘못된 비번입니다. 다시 입력하세요. >>> ")
print(" 축하합니다. 잠금이 해제되었습니다.")
print(unlock)









'''
user_input="!!잠금!! 비밀번호를 입력해 주세요 >>>   "

while  user_input != pwd:      
       print(wrong_pwd)
       user_input=input("잘못된 비밀번호 입니다. 다시 입력해 주세요 >>>   ")


print(unlock)
print("잠금이 해제되었습니다.")

'''    
