import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG, format='(%(threadName)-9s) %(message)s')

logging.debug('This message should go to the log file')

logging.info('So should this')

logging.warning('And this, too')
