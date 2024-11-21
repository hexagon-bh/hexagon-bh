import random

korea = 0
hanyang = 0

print("##################################")
print("고려대 한양대 생성기 (무조건 합격.)")
print("##################################")

input()

for i in range(1000):
    val = random.randint(1,2)
    if val == 1:
        print(str(i+1) + "번째 시도 : 한양대")
        korea += 1
    if val == 2:
        print(str(i+1) + "번째 시도 : 고려대")
        hanyang += 1

input()

print("##################################")
print("고려대 : " + str(hanyang))
print("한양대 : " + str(korea))
print("##################################")