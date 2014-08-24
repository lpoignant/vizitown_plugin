import logging
import sys
import os

from singleton import Singleton


@Singleton
class Logger:

    def __init__(self):
        self.logger = logging.getLogger('Vizitown-logger')
        self.logger.setLevel(logging.DEBUG)

        # Define file with entire path 
        loggerPath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../vizitown.log")

        fh = logging.FileHandler(loggerPath)
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)