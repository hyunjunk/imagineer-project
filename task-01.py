import random
cuisine =input("한식,중식,일식 중 한가지를 고르세요 ")


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
