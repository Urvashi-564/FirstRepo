import logging

class PracticeLogs:
    def test_loggingg(self):
        logger=logging.getLogger(__name__)
        fileHandler=logging.FileHandler("firstlogfile.log")

        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.debug("a debug staement ")
        logger.info("an information is printed")
        logger.warning("I am warning")
        logger.error("An error")
        logger.critical("I am critical")