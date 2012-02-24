#!/usr/bin/python
import os, time

SCRIPT_PATH = os.path.realpath(os.path.dirname(__file__))
FILE_PATH = '%s/developer-notify-out.txt' % SCRIPT_PATH
print FILE_PATH
f = open(FILE_PATH,'w')
out = 'Hi from Harp @ %s' % time.time()
print out
print >> f, out