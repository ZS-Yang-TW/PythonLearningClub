# 空字典
empty_dict = {}
empty_dict = dict()

# 建立字典
book = {"string": "123", "int": 123, "list": [123], "tuple": (123,)}
print(book)
book = dict(string = "123", int = 123, list = [123], tuple = (123,))
print(book)

# 利用雙值序列建立字典
# 傳入的雙值序列必須是可迭代的，且每個元素都只能有兩個值。
book = dict([("CH1", "Python基礎"), ("CH2", "流程控制"), ("CH3", "串列"), ("CH4", "字典")])
book = dict((["CH1", "Python基礎"], ["CH2", "流程控制"], ["CH3", "串列"], ["CH4", "字典"]))

# 利用 zip() 函式建立字典
chapter = ["CH1", "CH2", "CH3", "CH4"]
content = ["Python基礎", "流程控制", "串列", "字典"]
book = dict(zip(chapter, content))

# 用 [鍵] 來加入或修改字典中的元素
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
book["CH5"] = "函式"
print(book)
book["CH1"] = "前言與Python語言基礎"
print(book)

# 注意: 鍵的名稱必需是唯一的，如果有重複的鍵，後面的值會覆蓋前面的值。
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH3": "字典"}
print(book)

# 可以用 [鍵] 或 get() 來取得字典中的元素
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
print(book["CH1"])
print(book.get("CH1"))

# 用 .keys() 取得字典中所有的鍵。注意: 這個方法會回傳一個 dict_keys 物件，而不是 list
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
print(book.keys())
print(list(book.keys()))

# 用 .values() 取得字典中所有的值。注意: 這個方法會回傳一個 dict_values 物件，而不是 list
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
print(book.values())
print(list(book.values())) 

# 用 .items() 取得字典中所有的鍵值對。注意: 這個方法會回傳一個 dict_items 物件，而不是 list
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
print(book.items())
print(list(book.items()))

# 用 len() 可以取得字典中有多少個鍵值對
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH3": "字典"}
print(len(book))

# 用 {**字典1, **字典2} 來合併兩個字典。(原本的字典不會被改變)
book1 = {"CH1": "Python基礎", "CH2": "流程控制"}
book2 = {"CH3": "專案練習-減重App", "CH4": "專案練習-聊天機器人App"}
new_book = {**book1, **book2}
print(new_book)
print(book1)
print(book2)

# 用 .update() 來合併兩個字典。(前面的字典會被改變)
book1 = {"CH1": "Python基礎", "CH2": "流程控制"}
book2 = {"CH3": "專案練習-減重App", "CH4": "專案練習-聊天機器人App"}
book1.update(book2)
print(book1)
print(book2)

# 當兩個字典有重複的鍵時，後面的值會覆蓋前面的值
book1 = {"CH1": "Python基礎", "CH2": "流程控制"}
book2 = {"CH1": "專案練習-減重App", "CH2": "專案練習-聊天機器人App"}
print({**book1, **book2})

book1 = {"CH1": "Python基礎", "CH2": "流程控制"}
book2 = {"CH1": "專案練習-減重App", "CH2": "專案練習-聊天機器人App"}
book1.update(book2)
print(book1)

# 用 del 來刪除字典中的鍵值對
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
del book["CH4"]
print(book)

# 用 .pop() 來刪除字典中的鍵值對，並回傳被刪除的值。
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
print(book.pop("CH4"))
print(book)

# 用 .popitem() 來刪除字典中的最後一個鍵值對，並回傳被刪除的鍵值對。 (回傳的是一個 tuple)
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
print(book.popitem())
print(book)

# 用 .clear() 來刪除字典中的所有鍵值對
book = {"CH1": "Python基礎", "CH2": "流程控制", "CH3": "串列", "CH4": "字典"}
book.clear()
print(book)

# 用 in 來檢查字典中是否有某個鍵
user = {"msycomtw": "123456141", "steve1211": "654321", "pp0p1123": "987654"}
print("msycomtw" in user)

# 字典是可變的，因此在賦值時，要小心不要改到原本的字典
user = {"msycomtw": "123456141", "steve1211": "654321", "pp0p1123": "987654"}
user_revise = user
user_revise["msycomtw"] = "123456"
print(user)
print(user_revise)

# 為了避免上面的問題，可以用 .copy() 來複製一份字典
# 要記得，如果值是可變的，那麼在複製時，還是會改到原本的值。因此要用 deepcopy() 來複製。
user = {"msycomtw": "123456141", "steve1211": "654321", "pp0p1123": "987654"}
user_revise = user.copy()
user_revise["msycomtw"] = "123456"
print(user)
print(user_revise)

# 字典生成式
# 用 {key:value for key, value in zip(鍵的列表, 值的列表)} 來生成字典
words = "Pneumonoultramicroscopicsilicovolcanoconiosis"
letter_count = {letter: words.count(letter) for letter in words}
print(letter_count)

# 用 set 建立集合
empty_set = set()
print(empty_set)

# set 可以用來將可迭代物件的重複值去除
words = "aabdbabdbababdbabdabdba"
words_set = set(words)
print(words_set)

number = [0, 1, 0, 0, -1, 1, 1, 0, -1, 0]
number_set = set(number)
print(number_set)

# 用 len() 可以取得集合中有多少個元素
s = {1, 2, 3, 4, 5}
print(len(s))

# 用 add() 來新增元素到集合中
s = {1, 2, 3, 4, 5}
s.add(6)
print(s)


# 用 remove() 來刪除集合中的元素
s = {1, 2, 3, 4, 5}
s.remove(5)
print(s)

# set 是可迭代的，因此也可以用 for 迴圈來迭代
s = {1, 2, 3, 4, 5}
for i in s:
    print(i)
    
# 用 in 來檢查集合中是否有某個元素
drinks = {
    "QQㄋㄟㄋㄟ好喝到咩噗茶": {"珍珠","紅茶","鮮奶"},
    "紅茶拿鐵": {"紅茶","鮮奶"},
    "百香QQ綠茶": {"綠茶","百香果肉","珍珠","椰果"},
    "青檸冷萃": {"檸檬汁","綠茶","檸檬片"}
}

for drink, content in drinks.items():
    if "珍珠" in content:
        print(drink)
        
for drink, content in drinks.items():
    if "珍珠" in content and "鮮奶" not in content:
        print(drink)

# 交集
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print(set_1 & set_2)
print(set_1.intersection(set_2))

# 如果沒有交集，則回傳空集合
set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8}
print(set_1 & set_2)
print(bool(set_1 & set_2)) # 空集合會被當成 False

# 聯集
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print(set_1 | set_2)
print(set_1.union(set_2))

# 差集
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print(set_1 - set_2)
print(set_1.difference(set_2))

# 互斥或
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print(set_1 ^ set_2)
print(set_1.symmetric_difference(set_2))

# 集合的比較
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print(set_1 <= set_2) # 子集合
print(set_1.issubset(set_2)) # 子集合
print(set_1 <= set_1) # 所有的集合都是自己的子集合
print(set_1 < set_2) # 真子集合
print(set_2 >= set_1) # 超集合
print(set_2 > set_1) # 真超集合

# 集合的生成式
# 用 {item for item in 可迭代物件} 來生成集合
odd_number = {2*n+1 for n in range(100)}
print(odd_number)

# 集合是可變的，但是我們可以用 frozenset() 來生成不可變的集合
original_set = [1, 2, 3, 4, 5]
frozen_set = frozenset(original_set)
print(frozen_set)
#frozen_set.remove(1) # 會報錯，因為 frozen_set 是不可變的