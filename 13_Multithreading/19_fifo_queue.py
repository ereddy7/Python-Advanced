from queue import Queue
q=Queue(); [q.put(x) for x in (10,5,20,15)]
while not q.empty(): print(q.get(),end=" ")
