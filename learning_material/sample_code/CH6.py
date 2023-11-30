# while 迴圈
count = 1
while count <= 5:
    print(count)
    count += 1
    
# while True 可以建立無限迴圈，用 break 可以取消迴圈。
number = 0
while True:
    number = input("請輸入一個數字[輸入 q 離開]:")
    print(f"你輸入的是 {number}")
    
    if number == "q":
        print("掰掰！")
        break

# 用 continue 跳過一次循環，直接進入下一次循環。
number = 0
while True:
    number = input("請輸入一個數字[輸入 q 離開]:")
    if number == "q":
        print("掰掰！")
        break
    
    if number.isdigit() == False:
        print("這不是整數欸，我不想處理~")
        continue
    
    if int(number) % 2 == 0:
        print(f"{int(number)}，是一個偶數")
    else:
        print(f"{int(number)}，是一個奇數")
        
# 迴圈的 else 區塊
# 這個區塊會在迴圈結束後執行，除非迴圈中有 break 被執行。
numbers = "123456787654346237239"
check_offset = 0
while check_offset > len(numbers):
    if numbers[check_offset] == "9":
        print("找到 9 了！")
        break
    check_offset += 1
else:
    print("這個字串裡面沒有 9 唷！")
    
# for 迴圈
for i in range(5):
    print(i)
    
# 用 for 與 in 來迭代字串
words = "Just do it!"
for word in words:
    print(word)
    
# 用 for 與 in 來迭代串列
myList = [1, 2, 3, 4, 5]
for item in myList:
    print(item)
    
# 用 break 來中斷，或用 continue 來跳過迴圈。
words = "Just do it!"
for word in words:
    if word == " ":
        continue
    print(word)
    
words = "Just do it!"
for word in words:
    if word == "s":
        break
    print(word)

# 用 else 區塊來處理for迴圈結束後的事情。
words = "Just do it!"
for word in words:
    if word == "a":
        break
    print(word)
else:
    print("沒有找到 a 唷！")
    
# range() 函式 range(start, stop, step)
for i in range(5):
    print(i)
    
for i in range(1, 5):
    print(i)
    
for i in range(0, 11, 2):
    print(i)
    
# 用 while 迴圈 從 1 加到 100
sum = 0
number = 1
while number <= 100:
    sum += number
    number += 1
print(sum)

# 用 for 迴圈 從 1 加到 100
sum = 0
for number in range(1, 101):
    sum += number
print(sum)

# 因此，面對不同的問題，我們可以選擇不同的迴圈來解決。