import logging

my_logger = logging.getLogger('my')
my_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr = logging.FileHandler('my_logger.txt')
hdlr.setFormatter(formatter)
my_logger.addHandler(hdlr)