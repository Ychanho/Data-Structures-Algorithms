#리스트의 기초 - 변경 가능
list01 = []             #[] 빈 리스트
list02 = [1, 2, 3]      #[1, 2, 3]
list03 = ['a', 'b', 'c',]#['a', 'b', 'c'] 맨 마지막 원소에 쉼표를 써도 됨
list04 = list()             #[] 빈 리스트
list05 = list('abc')        #['a', 'b', 'c']문자열의 각 문자로부터 원소를 생성
list06 = list([1, ,2, 3])   #[1, 2, 3]리스트로부터 원소를 생성
list07 = list((1, 2, 3))    #[1, 2, 3]튜플로부터 원소를 생성
list08 = list({1, 2, 3})    #[1, 2, 3]집합으로부터 원소를 생성
list09 = list(range(7))         #[0, 1, 2, 3, 4, 5, 6]
list10 = list(range(3, 8))      #[3, 4, 5, 6, 7]
list11 = list(range(3, 12, 2))  #[3, 5, 7, 9, 11]
list12 = [None] * 5             #[None, None, None, None, None]
