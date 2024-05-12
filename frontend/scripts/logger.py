import os
import logging


def touch(fname, times=None):
    with open(fname, "a"):
        os.utime(fname, times)


def getLogger(app_name, log_path, reset=False):
    dirname = os.path.dirname(log_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    if os.path.isfile(log_path):
        if reset:
            os.remove(log_path)
            touch(log_path)
    else:
        touch(log_path)

    logging.basicConfig(
        filename=log_path,
        filemode="a",
        format="%(asctime)s,%(msecs)d - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )

    return logging.getLogger(app_name)


if __name__ == "__main__":
    logger = getLogger("MapBlaster", "./frontend/logs/output.log", True)
    logger.debug("hello world")
    logger.info("hello world")
    logger.warning("hello world")
    logger.error("hello world")
    logger.critical("hello world")
