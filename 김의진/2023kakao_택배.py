def solution(cap, n, deliveries, pickups):
    distance = 0
    remain_d = sum(deliveries)
    remain_p = sum(pickups)
    house_d = n-1
    house_p = n-1
    while(remain_d or remain_p):
        go = max(house_d, house_p)
        distance += ((go+1)*2)
        # 배달
        delivery = min(remain_d, cap)
        remain_d -= delivery
        while delivery and house_d>=0:
            amount = min(deliveries[house_d], delivery)
            delivery -= amount
            deliveries[house_d] -= amount
            while deliveries[house_d] == 0 and house_d>=0:
                house_d -= 1
        # 수거
        pickup = min(remain_p, cap)
        remain_p -= pickup
        while pickup and house_p>=0:
            amount = min(pickups[house_p], pickup)
            pickup -= amount
            pickups[house_p] -= amount
            while pickups[house_p] == 0 and house_p>=0:
                house_p -= 1
    return distance
'''
1. 가는길에 배달, 오는길에 수거해야함
2. 마지막집은 배달과 수거를 동시에 해야할듯
3. greedy? 그냥 마지막집부터 차례때로 배달 수거
4. 가장 먼 집을 처리하면서 나머지 집들 처리
'''