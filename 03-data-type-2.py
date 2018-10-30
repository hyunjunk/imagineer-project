# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# list []
print   ("list")
list_a = [1,2,3]
print   (list_a)
# print   (type([2,3,3]))
# index는 0부터 시작합니다.
# print   (list_a[0])
# print   (list_a[1])
# print   (list_a[2])

# slice -> : list 를 짜른다. 마지막 index 는 포함하지 않는다!
print   (list_a[0:1])
print   (list_a[0:2])

# append -> attach or supplement an element
list_a.append(4)
print   (list_a)

# remove -> remove a specific item from the set
list_a.remove(2)
print   (list_a)

# clear -> remove all the imtes from the set
list_a.clear()
print   (list_a)

# tuple (1,)
# print   ("tuple")
# print   ((1,2,3))
# print   (type((1,2,3)))

print   ("tuple")
tuple_a =   (1,2,3)
print   (tuple_a)
print   (type(tuple_a))
tuple_a.append(4)
# tuple 의 함수 내부 값은 변경 될 수 없다! 한번 생성 후

# dict (map) -> {} 사용
# key & value
dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
# 키와 값으로 분류 된다 "Apple" = key, "a type of truits" = "값"
print   (dict_a)
print   (dict_a["apple"])

# edit value
dict_a["pen"] = "something to write"
print   (dict_a)

# set set ([])
set_a = set([1,2,3])
set_b = set([2,4,6])
print   (set_a)
print   (set_b)

# 집합 - 교집합, 합집합, 차집합, 여집합
# 중복 제거에 유용
print   (set_a & set_b)
print   (set_a | set_b)
print   (set_a - set_b)
