class cleaner:
    def __init__(self, R, C, D, ROOM):
        self.r = R
        self.c = C
        self.d = D
        self.room = ROOM
        self.count = 0
        # 북 , 동 , 남 , 서
        self.di = [-1, 0, 1, 0]
        self.dj = [0, 1, 0, -1]

    def clean(self):
        if self.room[self.r][self.c] == 0:
            self.room[self.r][self.c] = -1
            self.count += 1
    
    def forward(self):
        if (0 <= self.r + self.di[self.d] < len(self.room)) and (0 <= self.c + self.dj[self.d] < len(self.room[0])):
            if self.room[self.r + self.di[self.d]][self.c + self.dj[self.d]] != 1:
                self.r = self.r + self.di[self.d]
                self.c = self.c + self.dj[self.d]

    def backward(self):
        back_d = (self.d + 2) % 4
        if (0 <= self.r + self.di[back_d] < len(self.room)) and (0 <= self.c + self.dj[back_d] < len(self.room[0])):
            if self.room[self.r + self.di[back_d]][self.c + self.dj[back_d]] != 1:
                self.r = self.r + self.di[back_d]
                self.c = self.c + self.dj[back_d]
                return True
        return False

    def find_cell(self):
        for i in range(1, 5):
            temp_d = (4 + (self.d-i)) % 4
            condition = self.room[self.r + self.di[temp_d]][self.c + self.dj[temp_d]]
            if condition == 0:
                return temp_d
        return -1

    def move(self):
        self.clean()
        n = self.find_cell()
        if n < 0:
            if self.backward():
                return True
            else:
                return False
        else:
            self.d = n
            self.forward()
            return True

def solution(N, M, R, C, D, ROOM):
    device = cleaner(R, C, D, ROOM)
    while(device.move()):
        pass
    return device.count

N, M = map(int, input().split())
R, C, D = map(int, input().split())
ROOM = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, M, R, C, D, ROOM))

'''
7 7
4 2 1
1 1 1 1 1 1 1
1 0 0 0 1 0 1
1 0 1 1 0 0 1
1 0 0 0 0 1 1
1 0 0 1 0 0 1
1 0 0 0 0 0 1
1 1 1 1 1 1 1
'''