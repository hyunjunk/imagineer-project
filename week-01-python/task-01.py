import random
cuisine = input("한식,중식,일식 중 한가지를 고르세요 ")


restaurant_한식 = ["The bibimbab","Arirang","Myungga"]
restaurant_중식 = ["수타짜장면","자금성","라이라이"]
restaurant_일식 = ["와사비","마약 타코아키","원조일본라면"]

if cuisine == "한식":
        print(random.choice(restaurant_한식))
elif cuisine == "중식":
        print(random.choice(restaurant_중식))
elif cuisine == "일식":
        print(random.choice(restaurant_일식))
else:
        print("한식,중식,일식 중에만 골라주세요")


# answer
# import random
#
# restaurant_한식 = ["The bibimbab","Arirang","Myungga"]
# restaurant_중식 = ["수타짜장면","자금성","라이라이"]
# restaurant_일식 = ["와사비","마약 타코아키","원조일본라면"]
#
# cuisine = input("한식,중식,일식 중 한가지를 고르세요 ")
#
# if cuisine == "한식" :
#     choice_result = random.choice(restaurant_한식)
# elif cuisine == "중식" :
#     choice_result = random.choice(restaurant_중식)
# elif cuisine == "일식" :
#     choice_result = random.choice(restaurant_일식)
# else :
#     print("한식, 중식, 일식 중에만 선택해주세요")
#
# if choice_result :
#     print("{} 중에서 {}가 선택 되었습니다.".format(cuisine,choice_result))
