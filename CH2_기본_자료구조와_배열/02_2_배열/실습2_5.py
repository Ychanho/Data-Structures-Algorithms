#실습2_5 튜플, 문자열, 문자열 리스트의 최댓값 구하기
# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

from max import max_of

t = (1, 4, 3, 4.5, 2, 3.14, 6)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')  #사전 순으로 출력됨
