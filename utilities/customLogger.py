import datetime
import inspect
import logging


class LogGen:
    @staticmethod
    def logGen(testName):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        dt = datetime.datetime.now()
        fileHandler = logging.FileHandler(f"Logs/automation - {testName} - {dt}.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s", datefmt="%d-%B-%Y %I:%M:%S %p")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
