# 5-5
# 스택으로 재귀 함수 구현하기(재귀를 제거)
from stack import Stack

def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break

x = int(input('정수값을 입력하세요.: '))

recur(x)