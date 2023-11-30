# 「#」是用來註解的符號，同時按下 「shift+"/"」 就可以打出來

# 你也可以用「'''」來增加一整個區段的註解。
'''
在這裡，
    你可以暢所欲言、自由換行
        自由換行
'''

# 有時候，我們會用---來分隔不同的區段
#---- 這個區塊不要動^^ ----#
print('就跟你說不要動！')
#---- 這個區塊不要動^^ ----#

# if else 的使用
rain = True
if rain: print('嗚嗚...不想出門ㄌ')
else: print('出去玩囉!')
    
# 如果要檢查的條件有多個，可以使用 elif
score = 4
if score == 5:
    print('非常滿意')
elif score == 4:
    print('滿意')
elif score == 3:
    print('普通')
elif score == 2:
    print('不滿意')
elif score == 1:
    print('非常不滿意')
else:
    print('數字應該在1~5之間')
    
# 「比較運算子> < >= <= ==」很常與「邏輯運算子 and or not」一起使用
temperature = 35
if temperature > 30:
    print("涼麵")
elif temperature > 20 and temperature <= 30:
    print("乾麵")
elif temperature <= 20 and temperature >= 10:
    print("拉麵")
elif temperature < 10:
    print("火鍋")

# 成員運算子 in ，可以用來檢查一個元素是否在一個序列中
myList = [1, 2, 3, 4, 5]
if 1 in myList:
    print('1 存在於 myList 中')
    
myWord = 'Hello World!'
if 'H' in myWord:
    print('H 存在於 myWord 中')

# 海象運算子 := (Python 3.8 之後才有)
# 在 Python 3.8 之前，我們要寫成這樣
myList = [1, 2, 3, 4, 5]
count = len(myList)
if count > 3:
    print(f"{count}這個數字大於3")

# 在 Python 3.8 之後，我們可以寫成這樣
myList = [1, 2, 3, 4, 5]
if (count := len(myList)) > 3:
   print(f"{count}這個數字大於3")


# 勘誤: 第61頁，「海象運算子」的範例
tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print(f"A fitting tweet")
else:
    print(f"Went over by {abs(diff)}")

tweet_limit = 280
tweet_string = "Blah" * 1000
if (diff := tweet_limit - len(tweet_string)) >= 0:
    print(f"A fitting tweet")
else:
    print(f"Went over by {abs(diff)}")
    