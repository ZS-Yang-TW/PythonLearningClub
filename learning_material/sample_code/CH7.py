# 建立 tuple
tuple_type1 = ()
tuple_type2 = 123,
tuple_type3 = (123,)
print(tuple_type1)
print(tuple_type2)
print(tuple_type3)

# 如果只加小括號，沒有逗號，建立出來的不會是 tuple
tuple_failed = (123)
print(tuple_failed)

# 指派有多個元素的 tuple 有很多方式。個人建議加上小括號比較安全
tuple_type4 = 123, 456, 789
tuple_type5 = 123, 456, 789,
tuple_type6 = (123, 456, 789)
print(tuple_type4)
print(tuple_type5)
print(tuple_type6)

# tuple 可以進行多重賦值，這種手法我們通常稱為「元組拆包 (tuple unpacking)」
number = (123, 456, 789)
a, b, c = number
print(a)
print(b)
print(c)

# 一般而言，如果我們要交換兩個變數，會額外利用一個暫存變數 temp 來協助交換：
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)


# 利用 tuple 拆包的概念，可以很方便地交換兩個變數的值
a = 1
b = 2
a, b = b, a
print(a, b)

# 當然，利用 tuple 進行多個值的交換也是可以的
a = 1
b = 2
c = 3
a, b, c = c, a, b
print(a, b, c)

# 可以把可迭代物件轉換成 tuple
words = 'abc'
my_tuple = tuple(words)
print(my_tuple)

# 可以用 + 來連接 tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

# 可以用 * 來重複 tuple
tuple1 = (1, 0)
tuple2 = tuple1 * 10
print(tuple2)

# 比較 tuple：可以用 == 來比較 tuple 是否相等；也可以用 > 或 < 來比較 tuple 的長度大小
tuple1 = (1, 2)
tuple2 = (1, 3)
tuple3 = (1, 2, 3)
print(tuple1 == tuple2)
print(tuple1 > tuple3)

# tuple 是可以迭代的
tuple1 = (1, 2, 3)
for i in tuple1:
    print(i)
    
# tuple 是不可變的！ 這也讓用 tuple 型態儲存的資料比較安全
t1 = (1, 2, 3)
# t1[0] = 4 # 這行會出錯

# 因為 tuple 是不可變的，所以重新指派的時候，會產生新的 tuple (id 已經不同了！)
t1 = (1, 2, 3)
print(id(t1))
t1 += (4,)
print(id(t1))

# 建立空串列
list_type1 = []
list_type2 = list()
print(list_type1)
print(list_type2)

# list() 可以將可迭代物件轉換成串列
my_list1 = list('abc')
my_list2 = list((1,2,3))
my_list3 = list(range(10))
print(my_list1)
print(my_list2)
print(my_list3)

# 用 split() 將字串轉換成串列，我們很常用這個技巧來將輸入的資料轉換成串列
number = input('請輸入數字，以空白鍵分隔：').split()
print(number)

# 可以用 [offset] 取得串列中的元素，但記得 offset 必需要是有效的
my_list = [1, 2, 3]
print(my_list[0])
print(my_list[-1])

# 可以用 slice 的方式取得串列中的元素，這些 slice 都不會改變原本的串列
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[0:2])
print(my_list[::-1])

# 如果要將原串列反轉，可以用 reverse()
print(my_list)
my_list.reverse()
print(my_list)

# 用 append() 可以將元素加到串列的最後面，但是只能加一個元素
my_list = ['apple', 'banana', 'orange']
print(my_list)
my_list.append('watermelon')
print(my_list)

# 用 insert() 可以將元素加到串列的任何位置
my_list = ['apple', 'cat', 'dog', 'egg']
print(my_list)
my_list.insert(1, 'banana')
print(my_list)

# 可以用 * 來重複串列
my_list = [0, 1, 1, 0]
print(my_list * 3)

# 可以用 extend() 來連接串列
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
print(id(my_list1))
print(id(my_list2))

my_list1.extend(my_list2)
print(my_list1)
print(id(my_list1))

# 可以用 += 來連接串列
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
print(id(my_list1))

my_list1 += my_list2
print(my_list1)
print(id(my_list1))

# 注意，如果用 append() 來連接串列，就會變成「串列中有串列」。記得不要誤用！
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list1.append(my_list2)
print(my_list1)

# 串列是可變的，所以我們可以用 [offset] 來修改串列中的元素
my_list = ['steven', 'Ivy', 'Eva']
my_list[0] = 'Steven'
print(my_list)

# 我們可以用 slice 來一次取代串列特定區間的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[0:3] = [0, 0, 0]
print(numbers)

# 使用 slice 來取代串列特定區間的元素時，兩邊的長度不一定要相同
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[0:3] = [0, 0, 0, 0, 0]
print(numbers)

# 甚至右邊不一定要是串列，只要是可迭代物件就可以!
numbers = [0,0,0,0,0,6,7,8,9]
numbers[0:5] = range(5)
print(numbers)

# 用 del 來刪除串列中的元素
members = ["Steven", "Ivy", "Eva", "Jack"]
del members[-1]
print(members)

# 如果你不確定要刪除的元素在哪裡，可以用 remove() 來刪除串列中的元素，但只會刪除第一個找到的元素
members = ["Steven", "Ivy", "Eva", "Jack"]
members.remove("Ivy")
print(members)

# 用 pop() 來「取出」串列中的元素。預設是取出最後一個元素，並且會將該元素會從原串列中刪除。
members = ["Steven", "Ivy", "Eva", "Jack"]
fired_member = members.pop()
print(fired_member)
print(members)

# 如果想取出第一個元素，可以用 pop(0)。(FIFO 的概念)
members = ["Steven", "Ivy", "Eva", "Jack"]
fired_member = members.pop(0)
print(fired_member)
print(members)

# 用 clear() 可以清空串列
members = ["Steven", "Ivy", "Eva", "Jack"]
members.clear()
print(members)

# 用 index() 可以找出元素在串列中的位置。如果有重複的元素，只會回傳第一個找到的位置。
members = ["Steven", "Ivy", "Eva", "Jack"]
print(members.index("Eva"))

# 用 in 來檢查元素是否在串列中
sentence = ["我","真","的","很","常","忘","記","加","句","點"]
print("。" in sentence)

# 用 count() 來計算元素在串列中出現的次數
numbers = [1, 0 ,1, 1, 1 ,0, 1, 1, 0 ,0]
print("同意票數： ", numbers.count(1))
print("反對票數： ", numbers.count(0))

# 用 join() 來將串列中的元素連接成字串
members = ["Steven", "Ivy", "Eva", "Jack"]
separator = " | "
print("成員名單: ", separator.join(members))

# 用 sort() 以及 sorted() 來排序串列中的元素
# sort() 是一種串列的方法，因此會直接改變原串列。
numbers = [1, 5, 3, 2, 4]
numbers.sort()
print(numbers)

# sorted() 是一種內建函式，會回傳一個新的串列，原串列不會被改變。
numbers = [1, 5, 3, 2, 4]
print(sorted(numbers))
print(numbers)

# sort() 以及 sorted() 都預設是由小到大排序，如果要由大到小排序，可以加上 reverse=True
numbers = [1, 5, 3, 2, 4]
numbers.sort(reverse=True)
print(numbers)

# 除了按照數字大小排序，sort() 以及 sorted() 也會按照字母順序排序
members = ["Steven","Ben", "Ivy", "Eva", "Jack", "Anna"]
members.sort()
print(members)

# 注意： 如果串列中的元素是數字與字串混合，就會出現錯誤
members = ["Steven", "Ben", "Ivy", "Eva", "Jack", "Anna", 1, 2, 3]
# members.sort() # 這行出現錯誤

# 用 len() 來計算串列長度
members = ["Steven", "Ben", "Ivy", "Eva", "Jack", "Anna"]
print(len(members))

# 還記得嗎? 因為串列是可變的。所以兩變數指向的串列被改變時，兩變數都會被改變喔! (因為都是同個串列嘛~)。
list_1 = [1, 2, 3]
list_2 = list_1
list_2[0] = 0
print(list_1)
print(list_2)

# 如果你想要複製一個串列，可以用 copy() 、list() 或是 [:] 來複製
# 被複製的串列會被放在新的記憶體位置，因此串列間就不會互相影響了！
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

print(id(a))
print(id(b))
print(id(c))
print(id(d))

# 如果串列中的元素是可變的(例如: 串列中有串列)，那麼使用串列間還是會互相影響!
# 因此，我們會改用 deepcopy() 來複製這種串列。
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 0
print(a)
print(b)

import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 0
print(a)
print(b)

# 比較串列 ：可以用 == 來比較串列是否相等；也可以用 > 或 < 來比較串列的長度大小
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a > b)

# 串列是可以迭代的，因此可以用 for 迴圈來走訪串列中的元素
members = ["Steven", "Ben", "Ivy", "Eva", "Jack", "Anna"]
for member in members:
    print(member)
    
# zip() 可以將多個串列中的元素一一配對，並且回傳一個可迭代的物件。
members = ["Steven", "Ben", "Ivy", "Eva", "Jack", "Anna"]
gender = ["M", "M", "F", "F", "M", "F"]
salary = [40000, 50000, 60000, 70000, 80000, 90000]

for member, gender, salary in zip(members, gender, salary):
    test = " | ".join([member, gender, str(salary)])
    print(test)
    
# zip() 可以用於快速建立二維串列或是字典。在處理資料映射時，zip() 會很好用。
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
print(list(zip(numbers, letters)))
print(dict(zip(numbers, letters)))

# 串列生成式 (List Comprehension) 是一種快速建立串列的方法。
# 串列生成式的語法是 [運算式 for 項目 in 可迭代項目]
# 串列生成式的運算式可以是任何運算式，例如: 一個數字、一個函式、一個字串等等。
square_number = [i**2 for i in range(1, 11)]
print(square_number)

# 串列生成式也可以加上條件式，來過濾串列中的元素。
even_number = [i for i in range(1, 11) if i % 2 == 0]
print(even_number)

# for迭代、條件式都可以一直疊上去，但是要注意可讀性。
multi_table = [f"{i} * {j} = {i*j}" for i in range(1, 10) for j in range(1, 10)]
print(multi_table)

# 串列也可以有串列，這種串列稱為二維串列。甚至可以有三維、四維、五維...的串列。
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_2d[2][0])