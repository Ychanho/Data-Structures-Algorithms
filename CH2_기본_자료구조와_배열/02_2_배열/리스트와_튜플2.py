#실습 2C_1
#리스트의 모든 원소를 스캔하기(원소 수를 미릭 파악)

x = ['John', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    # print(f'x[{i}] = {x[i]}')

#실습 2C_2
#리스트의 모든 원소를 enumerate()함수로 스캔하기

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x): # i, name 두개로 지정해줘여 함
    print(f'x[{i}] = {name}')

#실습 2C_3
#리스트의 모든 원소를 enumerate()함수로 스캔하기(1부터 카운트)

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1): # ,1 하면 1부터 카운트
    print(f'{i}번째 = {name}')

#실습 2C_4
#리스트의 모든 원소를 스캔하기(인덱스값을 사용하지 않음)

x = ['John', 'George', 'Paul', 'Ringo']

for i in x:
    print(i)




