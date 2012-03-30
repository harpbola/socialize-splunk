#!/opt/splunk/bin/scripts/socialize-splunk/pyenv/bin/python
import sys
from defs import log
from helper import post_comment, read_search

def argv_to_dict(argv):
    try:
        return dict(number_of_events = argv[1],
            search_terms = argv[2],
            saved_search_title = argv[4],
            alert_reason = argv[5],
            search_url = argv[6],
            search_file_path = argv[8]
        )
    except IndexError:
        return {}
              
def handle_search(kwargs):
    log( 'kwargs: %s' % kwargs)
    saved_search_title = kwargs.get('saved_search_title') if kwargs.get('saved_search_title') else 'script-called-directly'
    alert_reason = 'script-called-directly'
    
    # Create message
    entity_key = "socialize-status-main"
    if saved_search_title == '[PROD] Error - Internal Server - 5 min':
        message = '%s ERRORS in last 5 mins.' % ( kwargs['number_of_events'])
        
    elif saved_search_title == 'Summary -- HTTP by Hour':
        entity_key = 'http-requests'
        search_data = read_search(kwargs['search_file_path'])
        log( "search_data: %s" % search_data)
        message = "Avg. Response Time: %(average_reponse_time)s \n"\
            "Total Requests: %(request_count)s\n"\
            "Oauth Errors: %(failure_count)s\n"\
            "Server Errors: %(error_count)s\n"\
            % search_data[0]
        post_comment(entity_key, message)
        
    else:
        message = alert_reason
        post_comment(entity_key, message)
    log( 'locals: %s' % locals)
        
if __name__ == "__main__":
    argv = argv_to_dict(sys.argv)
    handle_search(argv)