import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Read .env variables
DATA_FOLDER = os.environ.get("DATA_FOLDER")
OUTPUT_FOLDER = os.environ.get("OUTPUT_FOLDER")
DATA_FILE = os.environ.get("DATA_FILE")
LOG_FILE = os.environ.get("LOG_FILE")
CONSUMER_FILE = os.environ.get("CONSUMER_FILE")

# Project absolute path
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Create complete path
DATA_PATH = join(PROJECT_DIR, DATA_FOLDER)
OUTPUT_PATH = join(PROJECT_DIR, OUTPUT_FOLDER)


class FileConf:
    class Paths:
        data = DATA_PATH
        output = OUTPUT_PATH

    class FileNames:
        queue_file = join(DATA_PATH, DATA_FILE)
        logger = join(PROJECT_DIR, LOG_FILE)
        consumer = join(PROJECT_DIR, CONSUMER_FILE)


class LogConf:
    path = FileConf.FileNames.logger
    format = '%(asctime)s %(levelname)s:%(message)s'
    datefmt = '%m/%d/%Y %I:%M:%S %p'

    @staticmethod
    def create(logging):
        logging.basicConfig(format=LogConf.format, filename=LogConf.path, datefmt=LogConf.datefmt, level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.StreamHandler())
        return logger
