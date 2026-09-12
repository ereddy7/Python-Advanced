import logging
logger=logging.getLogger("demo"); logger.setLevel(logging.DEBUG)
formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
console=logging.StreamHandler(); console.setLevel(logging.INFO); console.setFormatter(formatter)
file=logging.FileHandler("abc.log",mode="w"); file.setLevel(logging.ERROR); file.setFormatter(formatter)
logger.addHandler(console); logger.addHandler(file)
logger.debug("debug"); logger.info("info"); logger.error("error")
