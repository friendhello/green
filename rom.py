import random
import time

def strTimeProp(start, end, prop, frmt):
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + prop * (etime - stime)
    return int(ptime)

def randomDate(start, end, frmt='%Y-%m-%d'):
    return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))

def randomDateList(start, end, n, frmt='%Y-%m-%d %H:%M:%S'):
    return randomDate(start, end, frmt)

start = '2015-05-02 12:12:12'
end = '2021-11-19 00:00:00'
lenth = 10
print(randomDateList(start, end, lenth).split(' ')[0].split('-')[0])
