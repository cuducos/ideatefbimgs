import datetime
from random import randint


def season(m):
    m = int(m)
    if m in [12, 1, 2]:
        return 'Winter'
    elif m in [3, 4, 5]:
        return 'Spring'
    elif m in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

now = datetime.datetime.now()

FIELDS = ['volume', 'season', 'year', 'color']
PLACEHOLDERS = {
    'volume': 'Any number, e.g. %s ' % randint(10, 40),
    'season': season(now.month),
    'year': now.year,
    'color': 'Click and select any color'
}
