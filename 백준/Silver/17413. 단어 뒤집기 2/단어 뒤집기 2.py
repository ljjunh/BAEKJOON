# < : 나오면 전부다 출력append 뒤에 공백이 나와두 >가 없으면 출력 ㄴ
# > : 정상출력
from collections import deque
string = input() + " "
stack = deque([])
for i in string:
    if i == " " and ">" not in stack and "<" not in stack:
        while stack:
            print(stack.pop(), end = "")
        print(" ", end = "")
    elif i == ">":
        stack.append(i)
        while stack:
            print(stack.popleft(), end = "")
    elif i == "<":
        while stack:
            print(stack.pop(), end = "")
        stack.append(i)
    else:
        stack.append(i)