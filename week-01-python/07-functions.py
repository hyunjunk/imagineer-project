# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("hi, {}".format(name))

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"

# print("hello, {}".format(name1))
# print("hello, {}".format(name2))
# print("hello, {}".format(name3))
# print("hello, {}".format(name4))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)

# 입력값 O, 반환값 O
def sum(a, b):
    return a + b

# 입력값 O, 반환값 X
def hello_friends(name):
    print("hi, {}".format(name))

# 입력값 X, 반환값 O
def return_1():
    return 1

# 입력값 X, 반환값 X
def hello_world():
    print("hello world")

num_1 = return_1()
print(num_1)
