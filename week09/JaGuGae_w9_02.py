# Python 리스트를 이용한 우선순위 큐 구현
priority_queue = []                         # 빈 Python 리스트 구현, 시간 복잡도: O(1)

priority_queue.append(3)                    # append(item) 메소드로 enqueue(item) 구현, 시간 복잡도: O(1)
priority_queue.append(1)                    # if 정렬된 동적 배열을 사용했다면? -> append의 시간 복잡도: O(n)
priority_queue.append(2)
priority_queue.append(4)

smallest = priority_queue[0]                # Python 리스트에 저장되어 있던 항목 중 우선순위가 가장 높은 항목을 탐색 후
for i in priority_queue:                    # 탐색: 시간복잡도 O(n)
    if i < smallest:                        # 여기에서는 항목의 값이 작을수록 높은 우선순위를 가진다고 가정
        smallest = i                        # 이제 우선순위가 제일 높은거를 찾았는데, 이 값이 리스트의 어디에 존재한지를 찾아야 함.
index = priority_queue.index(smallest)      # 그 때 index 메소드를 사용한다.

result = priority_queue.pop(index)          # 해당 항목을 삭제 및 반환함으로서 dequeue(item) 구현,
                                            # 시간 복잡도: 자리 이동으로 인한 O(n)
                                            # if 정렬된 동적 배열을 사용했다면? -> dequeue의 시간 복잡도: O(1)

print(result)

"""
참고
항목의 삽입 위치는 맨 끝, 삭제 위치는 우선순위가 가장 높은 항목의 위치로만 제한하는 것이 더 바람직하다.
따라서 Python 리스트를 이용한 PriorityQueue 클래스를 정의하는 방법 또한 좋은 방법 중 하나이다.
"""