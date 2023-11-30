# 檢查型態的方式 type()
data1 = 2.3
print(type(2.3))

# 整數是不可變的
myNumber = 12
print(id(myNumber))
myNumber += 1
print(id(myNumber))

# 串列是可變的
myList = [1]
print(id(myList))
myList.append(2)
print(id(myList))

# 有些前後都加「雙底線」的變數很特別...
print(__name__)

# 「賦值」的真正意義是為資料取一個「名稱」當作命名標籤
data_a = 2

# 「多重賦值」就是在一個物件上，貼很多個命名標籤。
data_a = 2
data_c = data_b = data_a
print(id(data_a))
print(id(data_b))
print(id(data_c))

# 「重新賦值」就是你把命名標籤貼到另一個物件上了
data_d = 1
print(id(data_d))
data_d = 3
print(id(data_d))

# 對於不可變的物件來說，無法根據其中一個變數來更動參考的資料。 (x會重新指到新的物件)
x = 5
y = x
x = 37
print(x,id(x))
print(y,id(y))

# 對於可變的物件來說，可以根據其中一個變數來更動被參考的資料。 （x,y 指到的仍是同一的物件）
x = [1,2,3]
y = x
x[0] = 100
print(x,id(x))
print(y,id(y))