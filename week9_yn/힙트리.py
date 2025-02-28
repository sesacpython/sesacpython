### 힙 트리 (Heap Tree)

여러 개의 값 중에서 가장 크거나 작은 값을 빠르게 찾기 위해 만든 완전이진트리(complete binary tree , 모든 레벨이 가득 차 있걷나, 마지막 레벨에서 왼쪽부터 순서대로 채워진 트리)

최대 힙과 최소힙 두가지 종류 있음

-최대힙 max heap :부모노드가 자식 노드보다 크거나 같아야함

-최소힙 min heap : 부모노드가 자식 노드보다 작거나 같아야함 

*힙정렬 같은 정렬 알고리즘에 활용되며,배열을 이용해서 구현할수 있음(예시 인덱스 )

#최소힙
import heapq
heap = [] 
heapq.heappush(heap,4)
heapq.heappush(heap,3)
heapq.heappush(heap,8)
heapq.heappush(heap,7)

-------------------------

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
-------------------------
# 결과값
3
4
5
7
8


#최대힙
heap = []
heapq.heappush(heap,-9)
heapq.heappush(heap,-5)
heapq.heappush(heap,-7)
heapq.heappush(heap,-6)
heapq.heappush(heap,-2)
--------------------------
print(-heapq.heappop(heap))
print(-heapq.heappop(heap))
print(-heapq.heappop(heap))
print(-heapq.heappop(heap))
print(-heapq.heappop(heap))
--------------------------
#결과값
9
7
6
5
2
