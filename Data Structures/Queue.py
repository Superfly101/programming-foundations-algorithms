from collections import deque

# create empty deque
queue = deque()

# Add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print queue
print(queue)

# pop an item off front of the queue
x = queue.popleft()
print(x)
print(queue)
