import subprocess

from settings import FileConf


def execute_consumer(logger):
    logger.info("Function execute_consumer: executing consumer.sh file.")
    try:
        subprocess.call(FileConf.FileNames.consumer)
    except Exception as e:
        logger.warning("Function execute_consumer: error {}.".format(str(e)))
        raise("Error: {}".format(str(e)))
    logger.info("Function execute_consumer: execution completed.")
