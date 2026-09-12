import threading,time
def work(): time.sleep(1)
threads=[threading.Thread(target=work,name=f"Worker-{i}") for i in range(3)]
for t in threads:t.start()
print(threading.active_count(),[t.name for t in threading.enumerate()])
for t in threads:t.join()
