from queue import LifoQueue
q=LifoQueue(); [q.put(x) for x in (10,5,20,15)]
while not q.empty(): print(q.get(),end=" ")
