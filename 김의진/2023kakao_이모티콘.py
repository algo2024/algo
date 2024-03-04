def purchase(sales, emoticons, user_info):
    ratio, price = user_info
    total = 0
    interest = -1
    for sale, emoticon in zip(sales, emoticons):
        if sale >= ratio:
            total += (emoticon * ((100-sale)/100))
            if total >= price:
                return interest
    return total

from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    for sales in product(range(10, 50, 10), repeat=len(emoticons)):
        candidate = [0, 0]
        for user in users:
            result = purchase(sales, emoticons, user)
            if result < 0:
                candidate[0] += 1
            else:
                candidate[1] += result
        if answer[0] < candidate[0]:
            answer = candidate
        elif answer[0] == candidate[0] and answer[1] < candidate[1]:
            answer = candidate
    return answer
# 할인 경우의 수: 2^14=16384, -> 완전탐색