#실습2C_7
#자료형을 정하지 않은 리스트 원소 확인하기

x = [15, 64, 7, 3.14, [33, 55], 'abc']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

# 하나의 리스트 안에 여러 자료형을 사용할 수 있다.

#copy() 함수 주의 할 점 (얕은 복사)
x = [[1, 2, 3], [4, 5, 6]]
print(x)
y = x.copy()        #x를 y로 얕은 복사
print(y)
x[0][1] = 9
print(x)
print(y)            # copy한 후 x 리스트를 변경했다 해도 y까지 영향이 감

#copy의 decopy (깊은 복사) 구성원소 수준으로 복사하는 방법
import copy
x = [['a', 'b', 'c'], ['x', 'y', 'z']] ## x = [[a, b, c], [x, y, z]]
y = copy.deepcopy(x)
print(x)
print((y))
x[0][1] = 'k'
print(x)
print(y) #x 리스트를 변경했다 해도 y까지 영향이 안 감