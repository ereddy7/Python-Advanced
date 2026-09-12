from queue import Queue,LifoQueue,PriorityQueue
for Q in (Queue,LifoQueue,PriorityQueue):
    q=Q(); [q.put(x) for x in (10,5,20,15)]; print(Q.__name__,[q.get() for _ in range(q.qsize())])
