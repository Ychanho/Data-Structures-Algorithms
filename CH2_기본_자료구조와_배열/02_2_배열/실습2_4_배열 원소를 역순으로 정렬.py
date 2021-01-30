#실습 2-6
#뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i] #서로 교환

if __name__ == '__main__':  #현재 .py을 실행했을 때만 실행되는 문구
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.:'))
    x =[None] *nx #원소 수가 nx인 리스트 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))

    reverse_array(x)    #x를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')