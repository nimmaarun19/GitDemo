import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler) #filehandler object

    logger.setLevel(logging.INFO)
    logger.debug("This is debug statement from logger")
    logger.info("This is info from logger")
    logger.warning("This is warning from logger")
    logger.error("This is error from logger")
    logger.critical("This is critical from logger")