#!/opt/splunk/bin/scripts/socialize-splunk/pyenv/bin/python
import sys
from defs import log
from helper import post_comment, read_search

log( 'sys.argv: %s' % sys.argv )
saved_search_title = 'script-called-directly'
alert_reason = 'script-called-directly'
try:
    number_of_events = sys.argv[1]
    search_terms = sys.argv[2]
    saved_search_title = sys.argv[4]
    alert_reason = sys.argv[5]
    search_url = sys.argv[6]
    search_file_path = sys.argv[8]
    
    log(  '''
        number_of_events : '%(number_of_events)s'
        search_terms : '%(search_terms)s'
        saved_search_title : '%(saved_search_title)s'
        alert_reason : '%(alert_reason)s'
        search_url : '%(search_url)s'
        search_file_path : '%(search_file_path)s'
    ''' % locals() )
except IndexError:
    pass
    
# Create message
entity_key = "socialize-status-main"
if saved_search_title == '[PROD] Error - Internal Server - 5 min':
    message = '%s ERRORS in last 5 mins.' % (number_of_events)
elif saved_search_title == '[PROD] Access - 1 hour':
    message = 'Only %s requests in last hour. Kinda slow.' % (number_of_events)
elif saved_search_title == 'Summary -- HTTP by minute':
    entity_key = 'http-requests'
    search_data = read_search(search_file_path)
    log( "search_data: %s" % search_data)
    message = str(search_data[0])
else:
    message = alert_reason

post_comment(entity_key, message)