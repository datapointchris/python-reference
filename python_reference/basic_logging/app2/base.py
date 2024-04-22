import logging
import random


def app2_base_function():
    levels = (
        ('info', 'information'),
        ('warn', 'warning'),
        ('debug', 'debugging'),
    )
    level, message = random.choice(levels)
    logger = logging.getLogger(__name__)
    getattr(logger, level)(message)


app2_base_function()
