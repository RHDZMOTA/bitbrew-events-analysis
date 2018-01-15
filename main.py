import logging

from util.download import execute_consumer
from settings import LogConf
from optparse import OptionParser


def main(base_name, file_extension, logger):
    file_name = base_name + "." + file_extension
    pass


if __name__ == "__main__":
    logger = LogConf.create(logging)
    parser = OptionParser()
    parser.add_option("-u", "--update", action="store_true", help="Update the queue_log.txt file.")
    parser.add_option("-f", "--filename", type="string", help="Name of the output file. Default: analysis")
    parser.add_option("-p", "--pdf", action="store_true", help="PDF file extension.")

    kwargs, _ = parser.parse_args(args=None, values=None)

    if getattr(kwargs, "u"):
        execute_consumer(logger)

    file_base_name = getattr(kwargs, "filename") if kwargs.f else "analysis"
    file_extension = "pdf" if getattr(kwargs, "pdf") else "pdf"
    main(file_base_name, file_extension, logger)
