# 포인터로 연결 리스트 구현하기
#실습 8-1[A]

from __future__ import annotations
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""
        self.data = data    # 데이터
        self.next = next    # 뒤쪽 포인터

#실습 8-1[B]

class LinkedList:
    """연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.no = 0         #리스트에 등록되어 있는 노드의 개수
        self.head = None    #머리 노드에 대한 참조
        self.current = None #주목 포인터 (현재 주목하고 있는 노드에 대한 참조)

    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.no

# 실습 8-1[C]

    def search(self, data: Any) -> int:             # 검색을 수행하는 search()함수
            """data와 값이 같은 노드를 검색"""
            cnt = 0
            ptr =self.head
            while ptr is not None:
                if ptr.data == data:
                    self.current = ptr
                    return cnt
                    cnt += 1
                    ptr = ptr.next                  #ptr이 참조하는 곳이 다음 노드로 업데이트
            return -1                               #검색 실패
    def __contaions__(self, data: Any) -> bool:     #데이터가 포함되어 있는지 판단하는 함수
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return  self.search(data) >= 0

#실습 8-1[D] 머리에 노드를 삽입 하는 add_first()함수

    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를를 삽입"""
        ptr = self.head #삽입하기 전의 머리노드
        self.gead = self.current = Node(data, ptr)
        self.no += 1

#실습 8-1[E] 꼬리에 노드를 삽입 하는 add_last()함수

    def add_last(self, data: Any):
        """맨 끝에 노드를 삽입"""
        if self.head is None:       # 리스트가 비어 있으면
            self.add_first(data)    # 맨앞에 노드 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next  # while문을 종료할 때 ptr은 꼬리 노드를 참조
            ptr.next = self.current = Node(data, None)
            self.no += 1

#실습 8-1[F]

    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1

#실습 8-1[G]

    def remove_last(self):
        """꼬리 노드 삭제"""
        if self.head is not None:
            if self.head.next is None:  # 노드가 1개 뿐이라면
                self.remove_first()     # 머리 노드를 삭제
            else:
                ptr = self.head         # 스캔 중인 노드
                pre = self.head         # 스캔 중인 노드의 앞쪽 노드

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next  # while문 종료시 ptr은 꼬리 노드르르 참조하고 pre는 맨끝에서 두 번째 노드를 참조
                pre.next = None     # pre는 삭제 뒤 꼬리 노드
                self.current = pre
                self.no -= 1

#실습 8-1[H]
    def remove(self, p: Node) -> None:
        """임의의 노드 p를 삭제"""
        if self.head is not None:
            if p is self.head:          # p가 머리 노드이면
                self.remove_first()     # 머리 노드를 삭제
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return          # ptr은 리스트에 존재하지 않음
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None:    # 전체가 비어 있게 될 때까지
            self.remove_first()         # 머리 노드를 삭제
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """주목 노드를 한칸 뒤로 진행행"""
        if self.current is None or self.current.next is None:
            return False    #진행할 수 없음
        self.current = self.current.next
        return True

#실습 8-1[I]

    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

#실습 8-1[J]

    def __iter__(self) -> LinkedListIterator:
        """이터레이터(반복자)를 반환"""
        return LinkedListIterator(self.head)

class LinkedListIterator:
    """클래스 LinkedList의 이터레이터(반복자)용 클래스"""

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return  self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data