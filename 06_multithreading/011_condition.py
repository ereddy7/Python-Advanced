from threading import Thread,Condition
items=[]; condition=Condition()
def consumer():
    with condition:
        condition.wait_for(lambda: items); print("Consumed",items.pop())
def producer():
    with condition:
        items.append(42); print("Produced"); condition.notify()
Thread(target=consumer).start(); Thread(target=producer).start()
