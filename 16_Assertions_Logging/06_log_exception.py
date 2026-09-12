import logging
logging.basicConfig(filename="mylog.txt",level=logging.INFO)
try: print(10/0)
except ZeroDivisionError: logging.exception("Division failed")
