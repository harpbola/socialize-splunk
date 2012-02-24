import os
SCRIPT_PATH = os.path.realpath(os.path.dirname(__file__))
FILE_PATH = '%s/splunk-example-out.txt' % SCRIPT_PATH
log_file_handle = open(FILE_PATH,'w')
def log(message):
    global log_file_handle
    print message
    print >> log_file_handle, message