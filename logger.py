import os
import logging
import sys


curr_dir = os.path.dirname(os.path.abspath(__file__))

_formatter = logging.Formatter("%(asctime)s|%(jobid)s|encryptor|%(task_id)s|%(levelname)s|%(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(_formatter)
logger.addHandler(ch)


def decorate(func):
    def wrapper(*args, **kwargs):
        kwarg_defaults = {"extra":{"jobid":"","task_id":""}}
        kwarg_defaults.update(kwargs)
        func(*args, **kwarg_defaults)

    return wrapper

logger.error = decorate(logger.error)
logger.warn = decorate(logger.warn)
logger.debug = decorate(logger.debug)
logger.info = decorate(logger.info)
logger.exception = decorate(logger.exception)
