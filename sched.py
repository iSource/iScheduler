#!/usr/bin/python

from apscheduler.scheduler import Scheduler
from ConfigParser import ConfigParser
from jobs import *

config_file = 'jobs.conf'


if __name__ == '__main__':
    parser = ConfigParser()
    parser.read(config_file)
    sched = Scheduler(daemonic = False)

    for section in parser.sections():
        para = {}
        for (key, value) in parser.items(section):
            para[key] = value

        sched.add_cron_job(eval(section), day_of_week = para['day_of_week'], hour = para['hour'], minute = para['minute'], second = para['second'])

    sched.start()
