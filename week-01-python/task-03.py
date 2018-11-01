# 구현 내용
# - 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# - 사용자가 가위, 바위, 보를 고르면.
# 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# - 다합쳐 3번을 지거나, 3번을 이기면
# 게임은 최종 스코어를 보여 주면서 끝이 납니다.

# 1) 사용자 입력
# 2) 컴퓨터 임의 선택
# 3) 3번 지거나 이기면 승패 확정
import random

Rock = "바위"
Scissors = "가위"
Paper = "보"

RSP_List = (Rock, Scissors, Paper)

win_count = 0
lose_count = 0

while win_count < 3 and lose_count < 3 :
    user_choice = input ("{}, {}, {}".format(Scissors, Rock, Paper))

    computer_choice = random.choice(RSP_List)

    if user_choice == computer_choice :
        print("비겼습니다.")
    elif ((user_choice == Rock and computer_choice == Scissors) or (user_choice == Scissors and computer_choice == Paper) or (user_choice == Paper and computer_choice == Rock)) :
        win_count = win_count + 1
        print("이겼습니다.")
    else :
        lose_count = lose_count +1
        print("졌습니다.")

if win_count == 3 :
    print("사용자가 최종 승리하였습니다.")
else :
    print("컴퓨터가 최종 승리하였습니다.")
