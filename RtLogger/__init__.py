import logging

FORMAT = '%(asctime)s | %(message)s'

logging.basicConfig(format=FORMAT)


class RtLogger:
    def __init__(self, log_name=''):
        self.logger = logging.getLogger(log_name if log_name != '' else 'RayTracer')
        self.logger.setLevel(20)

    def __call__(self, message):
        self.info(message)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def __del__(self):
        self.logger.info("close application")
