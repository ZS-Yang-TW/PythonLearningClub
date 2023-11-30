# 定義一個「類別（class）」
class Cup():
    # 所有物件該具備的「屬性（attribute）」
    color = "white"
    
    # 所有物件該具備的「方法（method）」
    def pour(self):
        print("水被倒出來了")

# 將類別實例化(instantiate)成一個物件
my_cup = Cup()

# 呼叫物件現在具有的屬性與方法
print(my_cup.color)
my_cup.pour()

class Cat():
    def __init__(self, name):
        print(id(self))
        self.nammy = name
        pass
    
my_cat = Cat("Ketty")
print(id(my_cat))

class Dog():
    def __init__(this, name):
        this.name = name
        pass
    
    word = "Woof"
    
my_dog = Dog("Rex")
her_dog = Dog("Bella")


print(my_dog.word)
my_dog.word = "Bark"
print(her_dog.word)

# 定義新類別
class Cup():
    pass



class D():pass
class E():pass
class F():pass
class B(D, E):pass
class C(D, F):pass
class A(B, C):pass

print(A.mro())
print(A.__mro__)