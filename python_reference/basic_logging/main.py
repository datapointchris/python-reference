import logging
import random

import app1.base
import app1.home
import app2.base
import app2.home

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='./logs.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s: %(message)s <= `%(funcName)s` %(module)s:%(lineno)d %(pathname)s'
)
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)  # Exporting logs to the screen
logger.addHandler(fh)  # Exporting logs to a file


logger.info('info')


def main_function():
    levels = (
        ('info', 'information'),
        ('warn', 'warning'),
        ('debug', 'debugging'),
    )
    level, message = random.choice(levels)
    getattr(logger, level)(message)


main_function()
app1.base.app1_base_function()
app2.base.app2_base_function()
app1.home.app1_home_function()
app2.home.app2_home_function()
