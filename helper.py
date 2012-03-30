from settings import *
from oauth_hook import OAuthHook
import requests
import gzip, csv
import simplejson
from logging_helper import log

def read_gz(file_path):
    f = gzip.GzipFile(fileobj=open(file_path, 'rb'))
    data = f.read()
    return data

def csv_to_dict(file_path):
    reader = csv.reader(open(file_path), delimiter=',')
    headers = None
    content = []
    for row in reader:
        if headers is None:
            headers = row
        else:
            data = {}
            for i in xrange(len(row)):
                data[ headers[i] ] = row[i] 
            content += [data]
    return content
    
def read_search(file_path):
    data = read_gz(file_path)
    csv_file_path = file_path.replace('results.csv.gz', 'results_preview.csv')
    open(csv_file_path, 'w').write(data)
    return csv_to_dict(csv_file_path)
        
def make_partner_request(sub_url, payload):
    # create consumer and token
    OAuthHook.consumer_key = PARTNER_CONSUMER_KEY
    OAuthHook.consumer_secret = PARTNER_CONSUMER_SECRET
    oauth_hook = OAuthHook('', '', header_auth=True)

    url = PARTNER_API_BASE + sub_url
    body = {'payload' : simplejson.dumps(payload) }
    
    client = requests.session(hooks={'pre_request': oauth_hook})
    response = client.post(url, body)
    return response
           
def send_developer_notification():
    # create consumer and token
    OAuthHook.consumer_key = CONSUMER_KEY
    OAuthHook.consumer_secret = CONSUMER_SECRET
    oauth_hook = OAuthHook('', '', header_auth=True)

    url = "%s/application/%d/notification/" % (PARTNER_API_BASE, APPLICATION_ID)
    data = {"message" : message}
    sub_url = "/application/%d/notification/" % APPLICATION_ID
    payload = {'payload' : simplejson.dumps(data) }
    make_request(sub_url, payload)
    
def make_client_request(sub_url, payload):
    # create consumer and token
    OAuthHook.consumer_key = CONSUMER_KEY
    OAuthHook.consumer_secret = CONSUMER_SECRET
    oauth_hook = OAuthHook(TOKEN_KEY, TOKEN_SECRET, header_auth=True)

    url = CLIENT_API_BASE + sub_url
    body = {'payload' : simplejson.dumps(payload) }
    
    client = requests.session(hooks={'pre_request': oauth_hook})
    response = client.post(url, body)
    return response
        
def post_comment(entity_key, text):
    sub_url = "/comment/"
    payload = [{
        "entity_key" : entity_key, 
        "text": text
    }]
    response = make_client_request(sub_url, payload)
    log('Body: %s' % payload)
    log('Response status: %s' % response.status_code)
    log('Response content: %s' % response.content)
    return response