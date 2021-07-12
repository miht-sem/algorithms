from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(5)
q.popleft()
q.append(1)
q.append(1)
q.pop()

print(list(q))
