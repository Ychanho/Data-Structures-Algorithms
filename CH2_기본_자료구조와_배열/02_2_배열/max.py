#2_2_시퀀스_원소의_최댓값_출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a 원소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
         if a[i] > maximum:
            maximum = a[i]
    return maximum
#??? 현재 .py을 직접 실행할 때에만 참으로 간주됨 == 다른 스크립트 프로그램에서 임포트한 경우에는 거짓이 됨->if문 실행 안됨
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.:'))
    x = [None] * num  #원소 수가 num인 리스트를 생성
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))

    print(f'최댓값은 {max_of(x)}입니다.')