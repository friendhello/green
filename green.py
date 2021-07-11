# coding=gbk
import datetime,random,time
import os

# from heavy import special_commit

def strTimeProp(start, end, prop, frmt):
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + prop * (etime - stime)
    return int(ptime)

def randomDate(start, end, frmt='%Y-%m-%d'):
    return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))

def randomDateList(start, end, n, frmt='%Y-%m-%d %H:%M:%S'):
    return randomDate(start, end, frmt)

def modify():
    file = open('D:\GIthubWorkspace\Love-master\zero.md', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('D:\GIthubWorkspace\Love-master\zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    os.system('git commit -a -m "test"')


def set_sys_time():
    start = '2015-05-02 12:12:12'
    end = '2021-11-19 00:00:00'
    lenth = 10
    d = randomDateList(start, end, lenth).split(' ')[0].split('-')
    print(d)
    print('date %04d/%02d/%02d' % (int(d[0]), int(d[1]), int(d[2])))
    os.system('date %04d/%02d/%02d' % (int(d[0]), int(d[1]), int(d[2])))


def trick_commit(year, month, day):
    set_sys_time()
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        trick_commit(cur_date.year, cur_date.month, cur_date.day)

if __name__ == '__main__':
    daily_commit(datetime.date(2015, 5, 16), datetime.date(2016, 6, 17))