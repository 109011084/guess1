#產生一個隨機隨機整數1~100
#讓使用者重複數字去猜
#猜對了,要印出"你猜對了"
#猜錯了,要告訴他比答案大還是小
import random
r = random.randint(1,100)
while True:
    num = input('請輸入數字:')
    num = int(num)
    if num == r:
        print('你答對了')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')