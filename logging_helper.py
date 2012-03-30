import logging
import os
SCRIPT_PATH = os.path.realpath(os.path.dirname(__file__))
LOG_FILE_PATH = '%s/developer-notify-out.txt' % SCRIPT_PATH
L = None
def setup_logging():
    global L
    level = logging.DEBUG
    log_format = "%(asctime)s -- %(levelname)7s [%(process)d] [%(name)s:%(lineno)3d] - %(message)s"
    logging.basicConfig(format=log_format, filename=LOG_FILE_PATH)
    L = logging.getLogger('sz-status')
    L.setLevel(level)
    
setup_logging()

def log(message):
    L.debug(message)