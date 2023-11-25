import threading

# 공유 배열
shared_array = [[0,0], [0,0], [0,0], [0,0]]

# 락 리스트 생성
locks = [threading.Lock() for _ in shared_array]

def increment_element(index):
    global shared_array
    for _ in range(10):
        # 락을 획득
        locks[index].acquire()
        try:
            shared_array[index][0] += 1
            shared_array[index][1] += 1
        finally:
            # 락을 해제
            locks[index].release()

# 스레드 생성
threads = []
for i in range(1):
    thread = threading.Thread(target=increment_element, args=(i,))
    threads.append(thread)

# 스레드 시작
for thread in threads:
    thread.start()

# 스레드 종료 대기
for thread in threads:
    thread.join()

# 공유 배열 출력
print("Final shared array values:", shared_array)
