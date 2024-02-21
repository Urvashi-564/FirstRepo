import inspect
import logging

class ParentClass:
    def logging_demo(self):
        # loggername=inspect.stack()[1][3]
        loggerobj=logging.getLogger(__name__)
        # loggerobj = logging.getLogger(loggername)
        fileHandlerobj=logging.FileHandler("logfile.log")
        formatter=logging.Formatter("%(asctime)s:%(name)s:%(levelname)s")
        fileHandlerobj.setFormatter(formatter)
        loggerobj.addHandler(fileHandlerobj)
        loggerobj.setLevel(logging.DEBUG)
        return loggerobj