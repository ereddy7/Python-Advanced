from threading import BoundedSemaphore
s=BoundedSemaphore(2); s.acquire(); s.acquire(); s.release(); s.release(); print("balanced")
