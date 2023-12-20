import logging



def setup_logger_0():
    fmt = "%(asctime)s:%(name)s:%(levelname)s:%(message)s"
    lvl = logging.DEBUG
    logging.basicConfig(
            level=lvl, format=fmt, datefmt="%Y-%m-%d %H:%M:%S"
            )


def setup_logger_1(debug_mode=True, log_file="warup.log"):
    logger_format = "%(asctime)s:%(name)s:%(levelname)s:%(message)s"
    logging.basicConfig(
    level=logging.DEBUG, format=logger_format, datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger()

    # Console log
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    logger.addHandler(console_handler)

    # Log file
    log_file_handler = logging.FileHandler(log_file)
    logger.addHandler(log_file_handler)


def setup_logger_2(debug_mode=True, log_file="warup.log"):
    logger_format = "%(asctime)s:%(name)s:%(levelname)s:%(message)s"
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.setFormat(logger_format)

    # Console log
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    logger.addHandler(console_handler)

    # Log file
    log_file_handler = logging.FileHandler(log_file)
    logger.addHandler(log_file_handler)






if __name__=="__main__":
    setup_logger_2()
    lgr = logging.getLogger("main")

    #print("hello")
    lgr.info("hello")
    lgr.debug("hello")
