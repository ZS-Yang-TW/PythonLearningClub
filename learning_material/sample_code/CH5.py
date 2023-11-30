# 字串的表示方法
text_type_1 = '單引號字串'
text_type_2 = "雙引號字串"
text_type_3 = '''三引號字串，
    可以完整記錄文本的所有字元（包括換行與空格）。'''
text_type_4 = f"格式化字串，可以填變數與運算式，例如：{2**3}"
text_type_5 = r"原始字串，可以避免字元被轉譯。\n"
print(text_type_3)

# str()函式：將其他資料型態轉換為字串
print(str(123))
print(str(123.456))
print(str(True))

# print() 會將引號內的字串印出，並在每一個字串之間加上空格
print("Hello World", "and python", "and Math.")

# 空字串
empty_str = ""

# 常見的轉譯字元
text_1 = "換行\n"
text_2 = "TAB\t"
text_3 = "雙引號\""
text_4 = "斜線\\"
text_5 = "斜線\b"
print(text_1)
print(text_2)
print(text_3)
print(text_4)

text_type_5 = r"原始字串，可以避免字元被轉譯。\n"
print(text_type_5)

# 用「+」連接字串
word_1 = "我的名字是:"
word_2 = "小勝。"
sentence = word_1 + word_2
print(sentence)

# 小括號內的字串會自動連接，括號內的空格跟任何換行不會被保留
name = ("s" 
        "t" 
        "e" 
        "v"
        "e" 
        "n"
        )
print(name)

# 用「*」重複字串
laugh = "嗯"
laugh_die = laugh*10
print(laugh_die)

# 用 [] 取得字串中的字元
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[0])
print(letters[1])
print(letters[-1])

# 字串是不可變的，無法直接修改字串中的字元
word = "Hello"
# word[0] = "h"    #會出現錯誤

# 用 slice 取得子字串 [start:end:step]
letters = "abcdefgh"
print(letters[:])  # 取得全部字串
print(letters[2:]) # 取得 offset 2 之後的字串
print(letters[:7]) # 取到 offset 7 之前的字串 (僅取到 offset 7 - 1)
print(letters[-3:]) # 取倒數 3 個字元
print(letters [1:-3]) # 從 offset 1 開始，取到 offset -3 之前的字串
print(letters[::2]) # 每隔 2 個字元取得一個字元
print(letters[::-1]) # 反轉字串
print(letters[2:7:2]) # 組合技 - 從 offset 2 開始，每隔 2 個字元取得一個字元，直到 offset 7 為止

# 用 len() 取得字串長度
letters = "abcdefgh"
print(len(letters))

# 用 split() 將字串拆分
sentence = "I am a student."
print(sentence.split(" "))

items = "Apple,Banana,Orange"
print(items.split(","))

# 用 join() 將字串結合
items = ["Apple", "Banana", "Orange"]
print(",".join(items))

# 用 replace() 替換字串
sentence = "I am a student. The duty of a student is to learn."
print(sentence.replace("student", "teacher"))
print(sentence.replace("student", "teacher", 1))    # 第三個參數為替換次數

# 用 strip() 去除字串前後的字元
sentence = "   This is a title.   "
print(sentence.strip())
print(sentence.lstrip())
print(sentence.rstrip())

sentence = "   ..!!!! 商品大特賣 !!!!..   "
print(sentence.strip(" .!"))

# 用 startwith() 檢查開頭 ; 用 endswith() 檢查結尾
user_input = "!圖像生成 貓咪 翻滾 (彩色)"
print(user_input.startswith("!圖像生成"))
print(user_input.endswith("(彩色)"))

# 用 find() 及 index() 搜尋字串
lyrics = """上一篇文章被刪除後
所有叛逆的字元
決定不再讓空白 沈默
我們比空氣更自由
比時間還富有
沒有文字 無需言語 就能溝通"""

word = "字"
print(lyrics.find(word))
print(lyrics.index(word))

print(lyrics.rfind(word)) # 找最後一次出現的 offset
print(lyrics.rindex(word)) # 找最後一次出現的 offset

# 特殊判斷
print("123".isdigit()) # 判斷字串是否皆為「數字」
print("Abc123".isalnum()) # 判斷字串是否皆為「數字」或「英文字母」

# 大小寫處理
sentence = "so this is me swallowing my pride"
print(sentence.capitalize()) # 首字大寫
print(sentence.title()) # 每個單字的首字大寫
print(sentence.upper()) # 全部大寫
print(sentence.lower()) # 全部小寫
print(sentence.swapcase()) # 大小寫互換

# 字串對齊
start = "親愛的:"
end = "最愛你的人 敬上"
print(start.ljust(25))  # 左對齊
print(end.rjust(25))    # 右對齊

# 格式化字串(舊式，不推薦使用)
print("I'm %d years old." %  18)
print("My name is %s. I'm %d years old." % ("Steven", 18))

# 格式化字串(新式)
print("I'm {} years old.".format(18))
print("My name is {}. I'm {} years old.".format("Steven", 18))

name = "Steven"
age = 18
print("My name is {}. I'm {} years old.".format(name, age))
print("My name is {0}. I'm {1} years old.".format(name, age))   # 也可以用 index 指定參數

# 格式化字串(f-string，推薦使用)
name = "Steven"
age = 18
print(f"My name is {name}. I'm {age} years old.")
print(f"My sister name is Ivy. She is {age + 2} years old.") # 可以在 f-string 中做運算
print(f"{name.upper()}") # 可以在 f-string 中使用字串方法

# 想要直接印出變數的值，可以使用 f"{變數名稱=}" 這個格式，在除錯時很方便
num = 123
print(f"{num=}")

# 格式化的填補與對齊
author = "James Clear"
book = "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones"
pages = "320"
print(f"Author: {author:<15} Book: {book:<100},Pages: {pages:>5}")