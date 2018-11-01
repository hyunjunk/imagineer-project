

class Human:
    company = "잘살아보세 닷컴"


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender



class Colleague(Human):
    # position = "대리"
    def __init__(self, name, age, gender,position):
        super().__init__(name, age, gender)
        self.position = position


human1 = Colleague("김현준", 30,"남자", "과장")
human2 = Colleague("김철수", 29, "남자", "대리")
human3 = Colleague("김영희", 27, "여자", "대리")
human4 = Colleague("김지수", 25, "여자", "사원")

print(human1.name)
print(human2.age)
print(human1.__dict__)







#
# class Colleague(Human):
#     position = "직급"
#
#     def result(name, age, gender, potsition):
