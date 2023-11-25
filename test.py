import threading

shared_array = [0] * 5
locks = [threading.Lock() for _ in range(5)]

def modify_array(index, thread_id):
    global shared_array

    with locks[index]:
        for i in range(5):
            shared_array[index] += 1
            print(f"Thread {thread_id}: Element {index} is {shared_array[index]}      {shared_array}")

# 스레드 생성
threads = [threading.Thread(target=modify_array, args=(i, i+1)) for i in range(5)]

# 스레드 시작
for thread in threads:
    thread.start()

# 메인 스레드는 여기서 계속 실행됨

# 스레드가 종료될 때까지 대기
for thread in threads:
    thread.join()

# 이 부분은 스레드가 종료된 후에 실행됨
print("Final shared_array:", shared_array)
