# 利用 bool() 來判斷 True 或 False
# False的狀況(零，或空的)
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(None))

# True的狀況(有值)
print(bool(1))
print(bool(-1))
print(bool('0'))

# 可以用 + - 來表示數值
myNumber = +100
print(myNumber)

myNumber = -100
print(myNumber)

# 底數的表示方法(0b:二進位, 0o:八進位, 0x:十六進位 )
myNumber = 0b1010
print(myNumber)

myNumber = 0o0070
print(myNumber)

myNumber = 0xFFFF00
print(myNumber)

# 在數值中填入「,」，會轉變成元組(tuple)型態的資料。
myNumber = 1,000
print(myNumber)   

# 可以用 _ 來將數字做位數分隔
myNumber = 1_000
print(myNumber) 

# 整數運算
print(3+2)  #加
print(3-2)  #減
print(3*2)  #乘
print(3/2)  #浮點除法
print(3//2) #整除
print(3%2)  #取餘數
print(3**2) #次方

# 僅針對一個變數做運算，可以算術運算子」跟「賦值等號」連用
a = 100
a += 1      # 在 C 語言當中，會寫成 a++
print(a)

# 所有運算子都適用上面的簡化規則
a = 100
a *= 2      
print(a)

b = 100
b //= 3    
print(b)

# 請用括號表示清楚你的運算順序 (原則：拒絕猜測的誘惑)
ans = (2+3)+1*5

# int() 用於將字串轉換成整數、將浮點數取整、將布林值轉換成整數
print(int('123'))
print(int(123.456))
print(int(True))
print(int(False))

# 如果字串代表非十進位的數字，可以在 int() 中加入第二個參數，指定底數
print(int('1010',2))

# int() 無法處理有浮點數的字串
# print(int('123.456'))

# python 可以輕鬆處理大數運算 (別的語言要用陣列的方法來處理)
print(10**1000)

# float() 用於將字串轉換成浮點數、將整數轉換成浮點數
print(float('123.456'))
print(float(123))

# 浮點數可以在字母 e 後面加上十的次方數，類似科學記號
print(1.38e-3)

# 混合使用整數與浮點數，結果會自動轉換成浮點數
print(1+2.0)

# chr() 可以將數字轉換成字元 (ASCII)
print(chr(65))

# ord() 可以將字元轉換成數字 (ASCII)
print(ord('A'))

# A 往後數 3 個字元會是哪一個？
now = ord('A')
next = now + 3
print(chr(next))


# 偷偷告訴你，python 有內建的數學函式庫，可以直接使用很多數學函式
import math
print(math.pi)
print(math.sin(math.pi/2))
print(math.log(100,10))
print(math.floor(3.14))
print(math.ceil(3.14))
print(math.sqrt(2))
