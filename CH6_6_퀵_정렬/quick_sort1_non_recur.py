# 비재귀적인 퀵 정렬 구현하기
from DS_Algo_Python.CH4_스택과_큐.CH4_1_스택.stack import Stack
from typing import MutableSequence

def qsort(a:MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬(비재귀적인 퀵 정렬)"""
    range = Stack(right - left + 1)

    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()
        x = a[(left + right) // 2]

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push( (left, pr) )
        if right > pl: range.push( (pl, right) )

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('비재귀적인 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
