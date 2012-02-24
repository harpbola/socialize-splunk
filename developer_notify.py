#!/opt/splunk/bin/scripts/socialize-splunk/pyenv/bin/python
from settings import *
import simplejson, sys
from oauth_hook import OAuthHook
import requests
from defs import log

log( 'sys.argv: %s' % sys.argv )
try:
    number_of_events = sys.argv[1]
    search_terms = sys.argv[2]
    alert_title = sys.argv[4]
    alert_reason = sys.argv[5]
    
    log(  '''
        number_of_events : %s
        search_terms : %s
        alert_title : %s
        alert_reason : %s
    ''' % (number_of_events, search_terms, alert_title, alert_reason) )
except IndexError:
    pass
    
# create consumer and token
OAuthHook.consumer_key = CONSUMER_KEY
OAuthHook.consumer_secret = CONSUMER_SECRET
oauth_hook = OAuthHook('', '', header_auth=True)

# do it
url = "%s/application/%d/notification/" % (PARTNER_API_BASE, APPLICATION_ID)
data = {"message" : "Harp was here."}
body = {'payload' : simplejson.dumps(data) }

client = requests.session(hooks={'pre_request': oauth_hook})
response = client.post(url, body)
log('Response status: %s' % response.status_code)
log('Response content: %s' % response.content)