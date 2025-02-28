STACK / LAST IN FIRST OUT/ LIFO / 후입선출
-마지막에 들어간 데이터가 가장 먼저 나오는 구조라서 마지막에 추가한 데이터부터 사용해야 할때 유용 , 
되돌리기(undo), 사이트 방문기록을 예시로 들수 있음.
기능
데이터 삽입: push() / append()
데이터 삭제: pop()

큐 /QUE /FIRST IN FIRST OUT /FIFO /선입선출
-먼저 들어간 데이터가 먼저 나오는 구조.스택과의 반대되는 개념으로 
먼저 들어온 순서대로 처리해야할때 유용하고, 창구 대기표를 예시로 들수 있음 (작업 예약할때 굿)
기능
데이터 삽입: enqueue() / append()
삭제: dequeue() / popleft()
-----------------------------
#스택 
stack = []
stack.append(1)
stack.append(3)
stack.append(8)
stack.append(15)
stack.append(11)
-----------------------------
print(stack.pop())  
print(stack.pop())  
print(stack.pop()) 
print(stack.pop())  
print(stack.pop())  
-----------------------------
#결과값
11
15
8
3
1
-----------------------------
#큐 / deque
from collections import deque
queue = deque()
queue.append(8)
queue.append(15)
queue.append(11)
-----------------------------
print(queue.popleft())  
print(queue.popleft())  
print(queue.popleft()) 
-----------------------------
#결과값
8
15
11
-----------------------------
