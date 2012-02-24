#!/opt/splunk/bin/scripts/socialize-splunk/pyenv/bin/python
from settings import *
import simplejson, sys
from oauth_hook import OAuthHook
import requests
from defs import log

log( 'sys.argv: %s' % sys.argv )
saved_search_title = 'script-called-directly'
try:
    number_of_events = sys.argv[1]
    search_terms = sys.argv[2]
    saved_search_title = sys.argv[4]
    alert_reason = sys.argv[5]
    
    log(  '''
        number_of_events : %s
        search_terms : %s
        saved_search_title : %s
        alert_reason : %s
    ''' % (number_of_events, search_terms, saved_search_title, alert_reason) )
except IndexError:
    pass
    
# create consumer and token
OAuthHook.consumer_key = CONSUMER_KEY
OAuthHook.consumer_secret = CONSUMER_SECRET
oauth_hook = OAuthHook('', '', header_auth=True)

# Create message
if saved_search_title == '[PROD] Error - Internal Server - 5 min':
    message = '%d ERRORS in last 5 mins.' % (number_of_events)
elif saved_search_title == '[PROD] Access - 1 hour':
    message = 'Only %d requests in last hour. Kinda slow.' % (number_of_events)
else:
    message = saved_search_title
    
# do it
url = "%s/application/%d/notification/" % (PARTNER_API_BASE, APPLICATION_ID)
data = {"message" : message}
body = {'payload' : simplejson.dumps(data) }

client = requests.session(hooks={'pre_request': oauth_hook})
response = client.post(url, body)
log('Body: %s' % body)
log('Response status: %s' % response.status_code)
log('Response content: %s' % response.content)