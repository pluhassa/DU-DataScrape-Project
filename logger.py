import logging
import argparse 

parser= argparse.ArgumentParser()
parser.add_argument('--log_level', type=str, default='INFO', help='Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')

args=parser.parse_args()

logger = logging.getLogger('test_logger')
logger.setLevel(getattr(logging, args.log_level.upper(), logging.INFO))

handler = logging.FileHandler('test.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('This is an info message')

