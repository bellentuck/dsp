# Hint:  use Google to find python function

from datetime import datetime
import time


def days(t1, t2, date_format):
    """Computes the difference in days between two dates.

    t1: string representing start date (and time)
    t2: string representing stop date (and time)
    date_format: format string for date (and time)

    e.g.:
    days(01/01, 01/02, %m/%d) = 1
    days(01/01, 01/02, %d/%m) = 31
    """

    start = datetime.strptime(t1, date_format)
    stop = datetime.strptime(t2, date_format)
    delta = stop - start
    return delta.days

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
print days(date_start, date_stop, '%m-%d-%Y')

####b)  
date_start = '12312013'
date_stop = '05282015'
start = time.strftime('%D %H:%M', time.localtime(int(date_start)))
stop = time.strftime('%D %H:%M', time.localtime(int(date_stop)))
print days(start, stop, '%m/%d/%y %H:%M')

####c)  
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
print days(date_start, date_stop, '%d-%b-%Y')
