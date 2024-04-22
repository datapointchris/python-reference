import logging
import random

logger = logging.getLogger(__name__)


def app1_base_function():
    levels = (
        ('info', 'information'),
        ('warn', 'warning'),
        ('debug', 'debugging'),
    )
    level, message = random.choice(levels)
    getattr(logger, level)(message)


app1_base_function()
