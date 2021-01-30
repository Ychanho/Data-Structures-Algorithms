# #기수 변환하기(n진수 구하기)
# #실습2-7[A]
# #10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기
#
# def card_conv(x: int, r: int) -> str:   #x : 변환하기 전의 수 //r:변환하려는 진수
#     """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
#
#     d = ''  #변환 후의 문자열
#     dchar = '0123456789ABCDEDGHIJKLMNOPQRSTUVWXYZ'
#
#     while x > 0:
#         d +=dchar[x % r] #해당하는 문자를 꺼내 결합
#         x //= r  #x를 r로 나눈 나머지 값
#
#     return d[::-1]  #역순으로 반환

########################################################
#실습2-7[A] 수정버전  : 몫, 나머지 구하는 과정도 출력되게
def card_conv(x: int, r: int) -> str:
    """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d = ''          #변환 후의 문자열
    dchar = '0123456789ABCDEDGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x)) #변환하기 전의 자릿 수

    print(f'{r:2} |  {x:{n}d}')  #r값을 2자리로 출력 ' r'이런 식으로
    while x > 0:
        print('   +' + (n * 2) * '-')
        if x // r:
            print(f'{r:2} |  {x//r:{n}d} … {x % r}')
        else:
            print(f'     {x // r:{n}d} … {x % r}')
        d +=dchar[x % r] #해당하는 문자를 꺼내 결합
        x //= r  #x를 r로 나눈 나머지 값

    return d[::-1]  #역순으로 반환


########################################################
#실습 2-7[B]

if __name__ == '__main__':  # = 두번
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:         #음이 아닌 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.:'))
            if no> 0:
                break

        while True:     # 2~36진수의 정숫값을 입력받음
            cd = int(input('어떤 진수로 변환할까요?:'))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input('한번 더 변환할까요?(Y ... 예 / N ... 아니요):')
        if retry in {'N', 'n'}:
             break
