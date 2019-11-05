from datetime import datetime
import threading
from hashlib import md5
import time
def not_a_crutch(number):
    z = datetime.now()
    second = number % 60
    number = number // 60
    minute = number % 60
    number = number // 60
    hour = number % 24
    number = number // 24
    day = hour % 30
    number = number // 30
    mounts = number % 12
    numbers = number // 12
    years = numbers
    years = z.year + years
    mount = z.month + mounts
    day = z.day + day
    hour = z.hour + hour
    minute = z.minute + minute
    second = z.second + second
    microsecond = z.microsecond
    return z.replace(years,mount,day,hour,minute,second,microsecond)

class Cash:
    def __init__(self,timelive,infa):
        self.timelive = not_a_crutch(timelive)
        print(datetime.now())
        self.data = infa
        self.work = True

    def endtime(self):
        if self.timelive <= datetime.now():
            del Cash
        print('ещё жива')

a = Cash(7657865 , 'infa')
b = Cash(868687,'chto-to')
try:
    while a:
        a.endtime()
        time.sleep(2)


except:
    print('cash cleared')

def cash(timelive):
    def chekcash(funk):
        def wrapper(*arg,**kwarg):
            cashindex = md5(f'{funk.__name__} {arg} {kwarg}')

        return wrapper
    return chekcash
        

    


        
        
