#!/usr/bin/python
import shutil
import os

A = '/home/mjj/PWS/Sched/A'
B = '/home/mjj/PWS/Sched/B'

def moveFile():
    for file_name in os.listdir(A):
        f = os.path.join(A, file_name)
        if os.path.isfile(f):
            try:
                shutil.move(f, B)
                print '== Move ' + f + ' To B =='
            except Exception, e:
                print e

