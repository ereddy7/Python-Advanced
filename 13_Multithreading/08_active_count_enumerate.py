import threading,time
def job(): time.sleep(.2)
ts=[threading.Thread(target=job) for _ in range(3)]
for t in ts:t.start()
print(threading.active_count(),[t.name for t in threading.enumerate()])
for t in ts:t.join()
