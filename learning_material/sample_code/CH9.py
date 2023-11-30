# 定義空函式
def do_nothing():
    pass

do_nothing()

# 無參數函式：不需要任何參數就能執行的函式
def say_hello():
    print('Hello!')
    
say_hello()
    
# 用 return 設計函式的回傳值
def agree():
    return True

if agree():
    print('同意!')
else:
    print('不同意!')

# 引數與參數
def repeat(word):
    print(id(word))
    return word + ' ' + word

print(repeat('hey'))

# 補充：「Pass by Assignment」的概念
# 除非有重新賦值，要不然函式會讓「參數」所指向的資料，跟函式外「引數」指向的資料相同。
def add_element(a, b):
    # 這時如果該變數指向的資料是「可變的」。那只要這個變數指向的資料被修改，作用域外的另一個變數也會被修改。
    a.append(4)
    
    # 如果有重新賦值，則會在函式內產生一個指向的新資料的變數。因此，作用域外的變數就不會被修改。
    b = [1,2,3]
    b.append(4)
    
myList_a = [1,2,3]
myList_b = [1,2,3]
add_element(myList_a, myList_b)
print(myList_a)
print(myList_b)

# None: Python 中的「空值」
def give_nothing():
    pass

print(give_nothing())

# None 當作布林值判斷時，可以當 False 來用
# 下面這段程式碼，我們可以這樣解釋:「get存在嗎？如果存在，那...；如果不存在，那...」
get = give_nothing()
if get:
    print('有拿到東西')
else:
    print('空空如也')
    
# 位置性引數(Positional Argument)：填入引數時，需按照函式定義的順序填入
def set_style(color, font, size):
    return f'The style is \"color: {color}, font: {font}, size: {size}\"'
print(set_style('red', 'Arial', '20px'))
print(set_style('Arial', '20px', 'red')) ##亂調順序，會導致函式執行有誤

# 關鍵字引數(Keyword Argument)：填入引數時，可以不按照函式定義的順序填入，直接指定引數的名稱即可。
def set_style(color, font, size):
    return f'The style is \"color: {color}, font: {font}, size: {size}\"'
print(set_style(color='red', font='Arial', size='20px'))
print(set_style(size='20px', color='red', font='Arial')) ##不按照順序，也不會導致函式執行有誤

# 預設參數(Default Argument)：在定義函式時，就給定引數的預設值
def set_style(size, color='black', font='Arial'):
    return f'The style is \"color: {color}, font: {font}, size: {size}\"'

print(set_style('20px'))
print(set_style('20px', font='Arial'))
# print(set_style('20px','Arial')) #思考看看，這樣會有什麼問題呢？

# 請不要誤把預設參數，當作初始化變數使用！
# 因此除非有意為之，否則請避免用可變的資料型態當作預設參數
def one_element_list(element, output=[]):
    output.append(element)
    return output

print(one_element_list(1))
print(one_element_list(2))
print(one_element_list(3))

def one_element_list(element):
    output = []
    output.append(element)
    return output

print(one_element_list(1))
print(one_element_list(2))
print(one_element_list(3))

# 修正後，比較正確且較彰顯原始動機的做法。
def one_element_list(a, b=None):
    if b is None:
        b = []
    b.append(a)
    return b

print(one_element_list(1))
print(one_element_list(2))
print(one_element_list(3))

if __name__ == '__main__':
    my_list = [(i for i in range(10))]
    print(my_list)
    pass