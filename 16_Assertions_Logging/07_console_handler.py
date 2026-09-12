import logging
logger=logging.getLogger("demo"); logger.setLevel(logging.INFO); h=logging.StreamHandler(); h.setFormatter(logging.Formatter("%(name)s:%(levelname)s:%(message)s")); logger.addHandler(h); logger.info("info")
