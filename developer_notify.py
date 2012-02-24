from settings import *
import simplejson, sys
from oauth_hook import OAuthHook
import requests
from defs import log

log( 'sys.argv: %s' % sys.argv )
    
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