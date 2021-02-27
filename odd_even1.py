import random

f = open("log_짝홀.txt", 'w')
result = open('result_짝홀.txt','w')
# 같은 폴더에 파일 생성
class lift:
    def __init__(self):
        self.floor = 1
        # 현재 엘리베이터 위치
        self.direction = 0
        # 0 = stop, 1 = up, -1 = down        
        self.limit = 15
        # 정원
        self.num = 0
        # 현재 승객 수
        self.info=[]
        # 승객 정보 (도착 시간, 목표층, 탑승 시간)
        self.Call=[]
        # 엘리베이터 내부 버튼
        self.Up=[]
        # 외부 버튼 (상승)
        self.Down=[]
        # 외부 버튼 (하강)
    def add(self,k,call):
        if k not in call:
            call.append(k)
        # 요청 입력 함수
    def switch(self):
        if self.Call == []:
            if self.Up == [] and self.Down == []:
                self.direction = 0
            else:
                max_up = 0
                max_down = 0
                min_up = 100
                min_down = 100

                for i in self.Up:
                    if i > max_up:
                        max_up = i
                    if i < min_up:
                        min_up = i
                for i in self.Down:
                    if i > max_down:
                        max_down = i
                    if i < min_down:
                        min_down = i

                if self.direction == 1:
                    if max_up >= self.floor or max_down > self.floor:
                        pass
                    else:
                        self.direction = -1
                if self.direction == -1:
                    if min_up < self.floor or min_down <= self.floor:
                        pass
                    else:
                        self.direction = 1
        # 엘리베이터의 진행 방향을 결정하는 함수
        # 엘리베이터 안에 승객이 있거나 진행 방향에 요청이 있을 경우 방향 유지
        # 진행 방향 앞쪽에 있는 요청들을 모두 처리한 후, 반대 방향 요청 처리
        # 요청이 없을 경우, 엘리베이터 정지
    def move(self,k):

        global clock
        global total_delay
        global num_delay
        global total_service
        global num_service

        time = 0

        if k == 1:
            can_stop = [1,3,5]
        else:
            can_stop = [1,2,4]

        if self.direction == 1:
            self.floor += 1
        elif self.direction == -1:
            self.floor -= 1
        # 진행 방향에 따라 이동
        cur = self.floor
        # 현재 층
        stop = False
        # 멈춤 여부
        if cur in self.Call:
            # 현재층이 목표인 승객이 있는 경우
            stop = True
            # 엘베 일시정지
            self.Call.remove(cur)
            out = 0
            # 내린 승객 수
            rest = []
            # 엘베안에 남은 승객
            for i in self.info:
                if i[1] == cur:
                    total_service += clock - i[2]
                    # 서비스 시간 계산
                    num_service += 1
                    # 서비스를 마친 승객 +1
                    out += 1
                    # 승객 수 -1
                else:
                    rest.append(i)
                    # 남아있는 승객
            self.info = rest
            self.num -= out
            f.write(f'{clock:.3f} : (엘베 {k}) {cur}층에서 {out}명 하차 . (현재 인원 {self.num}명)\n')

        self.switch()
        # 엘리베이터의 방향 결정

        if self.direction == 1 and cur in self.Up:
        # 상승 중이고 현재 층에 윗방향 요청이 있는 경우
            stop = True
            # 엘베 일시정지
            rest = []
            # 현재층에 남는 승객
            In = 0
            # 탑승한 승객 수
            take_all = True
            # 대기 손님이 모두 탑승했는가?
            for i in cust[cur]:
                if i[1] > cur and i[1] in can_stop:
                # 목표층이 위에 있고 홀수층인 경우
                    if self.num < 15:
                    # 만원이 아닐 경우
                        i[2] = clock + time
                        # 탑승 시간 입력
                        self.info.append(i)
                        # 엘베에 승객 정보 추가
                        self.add(i[1],self.Call)
                        # 엘리베이터에 목표층 추가
                        self.num += 1
                        # 승객 수 +1
                        total_delay += clock - i[0]
                        # 딜레이 타임 계산
                        In += 1
                        # 탑승 손님 +1
                    else:
                        rest.append(i)
                        take_all = False
                else:
                    rest.append(i)    

            cust[cur] = rest

            if take_all == True:
                self.Up.remove(cur)
                # 진행 방향의 승객을 모두 태웠을 경우, 요청 삭제

            f.write(f'{clock:.3f} : (엘베 {k}) {cur}층에서 {In}명 탑승. (현재 인원 {self.num}명)\n')
            num_delay += In
            # 대기 마친 승객 +
            num_queue[cur] -= In
            # 대기 승객 수 -    
            self.switch()
            # 엘리베이터 방향 결정

        if self.direction == -1 and cur in self.Down:
        # 하강 중이고 현재 층에 아랫방향 요청이 있을 경우
            stop = True
            # 엘베 일시정지
            rest = []
            # 현재층에 남는 승객
            In = 0
            # 탑승한 승객 수
            take_all = True
            # 대기 손님이 모두 탑승했는가?
            for i in cust[cur]:
                if i[1] < cur and i[1] in can_stop:
                # 목표층이 아래에 있고 짝수층인(1층 포함) 경우
                    if self.num < 15:
                    # 만원이 아닐 경우
                        i[2] = clock + time
                        # 탑승 시간 입력
                        self.info.append(i)
                        # 엘베에 승객 정보 추가
                        self.add(i[1],self.Call)
                        # 엘리베이터에 목표층 추가
                        self.num += 1
                        # 승객 수 +1
                        total_delay += clock - i[0]
                        # 딜레이 타임 계산
                        In += 1
                        # 탑승 손님 +1
                    else:
                        rest.append(i)
                        take_all = False
                else:
                    rest.append(i)    

            cust[cur] = rest

            if take_all == True:
                self.Down.remove(cur)
                # 진행 방향의 승객을 모두 태웠을 경우, 요청 삭제

            f.write(f'{clock:.3f} : (엘베 {k}) {cur}층에서 {In}명 탑승. (현재 인원 {self.num}명)\n')
            num_delay += In
            # 대기 마친 승객 +
            num_queue[cur] -= In
            # 대기 승객 수 -    
            self.switch()
            # 엘리베이터 방향 결정

        if self.direction == 0:
            # 엘리베이터가 정지했을 경우, 다음 move 이벤트 생성 X
            event_time[k+4] = 1.0e+30
            f.write(f'{clock:.3f} : (엘베 {k}) 정지. (현재 위치 {self.floor}층) \n')
        else:
            if stop == True:
            # 멈춰있었을 경우 
                event_time[k+4] = clock + 0.05 + 0.33
            else:
                event_time[k+4] = clock + 0.05
            # 이동시간:3초, 일시정지(열리고 닫히는 시간): 20초, move 이벤트 생성



lift1=lift()
lift2=lift()
# 객체 생성
end_time = 500
# 종료 시간
clock = 0.0
next_event = 7
num_queue = [0,0,0,0,0,0]
# 층별 대기 인원
cust = [[],[],[],[],[],[]]
# 층별 대기 승객 정보
event_time = [2*random.random(),3*random.random(),3*random.random(),3*random.random(),3*random.random(),1.0e+30,1.0e+30,end_time]
# 0~4: 승객 도착 (arrival), 5: 엘리베이터 1 이동 (move1), 6: 엘리베이터 2 이동 (move2), 7: 종료 시간
total_num_queue = [0,0,0,0,0]
total_num_lift = [0,0]
util_lift = [0,0]
total_delay = 0
num_delay= 0
total_service = 0
num_service = 0
# 통계값 저장

def update(last_time):
    time = clock - last_time
    for i in range(5):
        total_num_queue[i] += time * num_queue[i+1]
    total_num_lift[0] += time * lift1.num
    total_num_lift[1] += time * lift2.num
    if lift1.direction != 0:
        util_lift[0] += time
    if lift2.direction != 0:
        util_lift[1] += time 
    # 통계값 업데이트

def stat():
    # 결과값 계산 및 출력
    ave_num_queue = [round(i/end_time,2) for i in total_num_queue]
    ave_num_lift = [round(j/end_time,2) for j in total_num_lift]
    utilization = [round(k/end_time,4) for k in util_lift]
    ave_delay = round(total_delay/num_delay,3)
    ave_service = round(total_service/num_service,3)
    result.write(f'층별 평균 대기 인원: {ave_num_queue} \n')
    result.write(f'엘리베이터 평균 고객 수: {ave_num_lift} \n')
    result.write(f'엘리베이터 이용률: {utilization} \n')   
    result.write(f'평균 대기 시간: {ave_delay} \n')
    result.write(f'평균 서비스 시간: {ave_service} \n')
    result.write(f'처리한 고객 수(대기,서비스): {num_delay,num_service}\n')

def timing():

    # 다음 이벤트 결정

    global clock
    global next_event

    min_time = 1.0e+29

    for i in range(8):
        if event_time[i] < min_time:
            min_time = event_time[i]
            next_event = i
    
    clock = min_time

def arrival(k):

    global clock
    global total_delay
    global num_delay
    global total_service
    global num_service

    arrival_time = clock
    # 도착 시간
    n = random.randrange(1,5)
    # 도착 인원 수
    if k == 1:
        goal = random.randrange(2,6)
    else:
        goal = 1
    # 목표층 생성
    f.write(f'{clock:.3f} : {k}층에서 {goal}층으로 가는 고객 {n}명이 도착했습니다.\n')
    # 승객 생성
    if lift1.direction == 0 and lift1.floor == k and goal in [1,3,5]:
    # 엘리베이터 1이 현재 층에서 대기중인 경우
        lift1.num += n
        num_delay += n
        # 엘베 승객 및 대기 끝낸 승객 수 업데이트
        for i in range(n):
            lift1.info.append([arrival_time, goal, arrival_time])
        # 승객 정보 엘리베이터에 추가
        lift1.add(goal,lift1.Call)
        # 요청 입력
        if goal > lift1.floor:
            lift1.direction = 1
        else:
            lift1.direction = -1
        # 방향 결정
        event_time[5] = clock + 0.33 + 0.05
        # 20초후 move 이벤트 생성
        f.write(f'{clock:.3f} : (엘베 1) {k}층에서 승객 {n}명 탑승. (현재 인원 {lift1.num}명).\n' )
    elif lift2.direction == 0 and lift2.floor == k and goal in [1,2,4]:
    # 엘리베이터 2가 현재 층에서 대기중인 경우
        lift2.num += n
        num_delay += n
        # 엘베 승객 및 대기 끝낸 승객 수 업데이트
        for i in range(n):
            lift2.info.append([arrival_time, goal, arrival_time])
        # 승객 정보 엘리베이터에 추가
        lift2.add(goal,lift2.Call)
        # 요청 입력
        if goal > lift2.floor:
            lift2.direction = 1
        else:
            lift2.direction = -1
        # 방향 결정
        event_time[6] = clock + 0.33 + 0.05
        # 20초후 move 이벤트 생성
        f.write(f'{clock:.3f} : (엘베 2) {k}층에서 승객 {n}명 탑승 (현재 인원 {lift2.num}명).\n')
    else:
        # 두 엘리베이터가 다른 층에 있거나 움직이고 있는 경우
        num_queue[k] += n
        # 대기 인원 갱신
        for i in range(n):
            cust[k].append([arrival_time, goal, 0])
        # 대기 승객 정보 추가
        if k == 1:
            if goal in [1,3,5]:
                lift1.add(k,lift1.Up)
            if goal in [1,2,4]:
                lift2.add(k,lift2.Up)
        else:
            if k in [1,3,5]:
                lift1.add(k,lift1.Down)
            if k in [1,2,4]:
                lift2.add(k,lift2.Down)
        # 요청 입력
        if lift1.direction == 0 and (k in lift1.Up or k in lift1.Down):
            if k > lift1.floor:
                lift1.direction = 1
            else:
                lift1.direction = -1
            event_time[5] = clock + 0.05
            f.write(f'{clock:.3f} : (엘베 1) {k}층으로 이동.\n')
        # 엘리베이터 1이 정지해 있었을 경우, move 이벤트 생성
        if lift2.direction == 0 and (k in lift2.Up or k in lift2.Down):
            if k > lift2.floor:
                lift2.direction = 1
            else:
                lift2.direction = -1
            event_time[6] = clock + 0.05
            f.write(f'{clock:.3f} : (엘베 2) {k}층으로 이동.\n')
        f.write(f'{clock:.3f} : {k}층 대기 인원 {num_queue[k]}명.\n')
        # 엘리베이터2가 정지해 있었을 경우, move 이벤트 생성
    if k == 1:
        event_time[0] = clock + 1*random.random()
    elif k == 2:
        event_time[1] = clock + 2*random.random()
    elif k == 3:
        event_time[2] = clock + 2*random.random()
    elif k == 4:
        event_time[3] = clock + 2*random.random()
    else:
        event_time[4] = clock + 2*random.random()
    # 다음 arrival 이벤트 생성

def main():
    
    global clock
    global end_time
    global next_event

    while clock < end_time:
        last_time = clock
        timing()
        update(last_time)

        if next_event < 5:
            arrival(next_event+1)
        elif next_event == 5:
            lift1.move(1)
        elif next_event == 6:
            lift2.move(2)
        else:
            update(last_time)
            stat()
            print('종료')

main()
f.close()
result.close()