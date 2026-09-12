import logging
logger=logging.getLogger("demo_file"); logger.setLevel(logging.INFO); h=logging.FileHandler("abc.log",mode="w"); h.setFormatter(logging.Formatter("%(levelname)s:%(message)s")); logger.addHandler(h); logger.error("error")
