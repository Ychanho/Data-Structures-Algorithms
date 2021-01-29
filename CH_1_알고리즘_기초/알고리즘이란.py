# #01-1 알고리즘이란?
#
# #1-1 세 정수의 최댓값 구하기
# print('세 정수의 최댓값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요. :'))
# b = int(input('정수 b의 값을 입력하세요. :'))
# c = int(input('정수 c의 값을 입력하세요. :'))
#
# maximum = a
# if b  > maximum: maximum = b
# if c  > maximum: maximum = c
#
# print(f'최댓값은 {maximum}입니다.')3
# #input() :입력받은 문자열을 반환함 , int() : ()안에 들어 있는 문자열을 정수형으로 변환, float()은 실수형
#
# #1C-1 이름을 입력받아 인사하기
# print('이름을 입력하세요.:', end = '')
# name = input()0
# print(f'반갑습니다! {name}님.')
#{}하는 이유
#
# # 위와 동일한 결과
# name = input('이름을 입력하세요.:')
# print(f'반갑습니다.{name}님.')

# #p.s 문자열을 정수로 변환한 예
# n1 = int('17')
# n2 = int('0b110', 2)
# n3 = int('0o75', 8)
# n4 = int('13', 10)
# n5 = int('0x3F', 16)
# n6 = float('3.14')
# print(n1, n2, n3, n4, n5, n6)

#1-2 세 정수의 최댓값 구하기
# def max3(a, b, c):
#     """a,b,c의 최댓값을 구하여 변환"""
#     maximum = a
#     if b > maximum: maximum = b
#     if c > maximum: maximum = c
#     return maximum # 최댓값 반환
# print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
# print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')

# #p.s
# if a < b:
#     min2 = a
#     max2 = b
#
# if a < b: min2 = a; max2 =b  #위와 아래가 같은 결과를 낸다

# #1C-2 세 정수의 중앙값 구하기
# def med3(a, b, c):
#     """a,b,c의 중앙값을 구하여 반환"""
#     if a > b:
#         if b >= c:
#             return b
#         elif a <=c:
#             return a
#         else:
#             return c
#     elif a > c:
#         return a
#     elif b > c:
#         return c
#     else:
#         return b
#
# print('세 정수의 중앙값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.:'))
# b = int(input('정수 b의 값을 입력하세요.:'))
# c = int(input('정수 c의 값을 입력하세요.:'))
#
# print(f'중앙값은 {med3(a, b, c)}입니다.')
#
# #1C-2-1
# def med3(a, b, c):
#     """a,b,c의 중앙값을 구하여 반환(2번째 방법)"""
#     if (b >= a and c <= a) or (b <= a and c >= a):
#         return  a
#     elif(a > b and c <b) or (a < b and c < b):
#         return b
#     return c  # a와 비교를 이미 마친 상태에서 다시 비교하는 것이기 때문에 비효율적이다.

#1-3 입력받은 정수의 부호(양수, 음수, 0)출력하기
#
# n = int(input('정수를 입력해주세요.:'))
#
# if n > 0:
#     print('이 수는 양수입니다.')
# elif n == 0:
#     print('이 수는 0입니다.')
# else:
#     print('이 수는 음수입니다.')

#1-4 n이 1이면 A를, 2이면 B를, 이외는 C출력
n = int(input('정수를 입력해주세요.'))

if n == 1:
    print('A')
elif n == 2:
    print('B')
else:
    print('C')

#1-5 n이 1이면 A를, 2이면 B를, 3이면 C출력 이외는 아무것도 출력 안 함
n = int(input('정수를 입력해주세요.'))
if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')


#1-6 1-5와 같은 내용
n = int(input('정수를 입력해주세요.'))
if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
else:
    pass


