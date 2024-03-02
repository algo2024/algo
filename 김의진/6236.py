# M개의 K크기의 버킷에 인출금액을 차례대로 담을 때 K의 최솟값
N, M = map(int, input().split())
withdraw = [int(input()) for _ in range(N)]

def check(N, M, withdraw, K):
    remain = 0
    count = 0
    for cost in withdraw:
        if cost > K: return False
        # 인출해야하는 경우
        if remain < cost:
            remain = K
            count += 1
        remain -= cost
        if count > M:
            return False
    return True

def solution(N, M, withdraw):
    start = 0
    end = 2000000000
    while (start <= end):
        mid = (start + end) // 2
        if check(N, M, withdraw, mid):
            end = mid - 1
        else:
            start = mid + 1
    return start

print(solution(N, M, withdraw))