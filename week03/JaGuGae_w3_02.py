# 흐름 제어: line by line으로 실행되는 흐름을 마음대로 바꾸고 제어할 수 있음. 대표적으로 조건문, 반복문이 있음
# 조건문: if문
"""
if 조건식:
    명령문
else:
    명령문

*만약 여러 조건으로 세부화 시켜야 할 경우
if 조건식:
    명령문
elif 조건식:
    명령문
...
else:
    명령문
"""
s = "sweet"
if s == "sweet":
    print("삼킨다")
else:
    print("뱉는다")

num = 3
if num > 0:
    print("{}은 양수".format(num))
elif num < 0:
    print("{}은 음수".format(num))
else:
    print('0')

# 반복문: for문, while문
"""
for 변수 in iterable:
    반복 실행할 명령문
    ...

for 변수 in range(start, stop, step):
    반복 실행할 명령문
    ...
"""
num1 = 0; num2 = 0
for i in [1, 2, 3, 4, 5]:
    num1 += 1
    print(num1, end = "/////")
print("")

for i in "hello, world.":
    num2 += 1
    print(num2, end = "/////")
print("")

print(num1)
print(num2)

num1 = 0; num2 = 0; num3 = 0

# stop
for i in range(10):
    num1 += 1
    print(num1, end="/////")
print("")

# start, stop
for i in range(1, 10):
    num2 += 1
    print(num2, end="/////")
print("")

# start, stop, step
for i in range(1, 10, 2):
    num3 += 1
    print(num3, end="/////")
print("")

print(num1)
print(num2)
print(num3)

"""
while 조건문:
    명령문
    ...
"""
num = 23; running = True
while running:
    guess = int(input("Enter an integer: "))

    if guess == num:
        print("Congratulations, you guessed it.")
        # this causes the while loop to stop
        running = False
    elif guess < num:
        print("No, it is a little higher than that.")
    else:
        print("No, it is a little lower than that.")
print("Done.")