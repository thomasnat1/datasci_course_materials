import oauth2 as oauth
import urllib2 as urllib
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "idB3X5sdbEc3AgEuW8yCfR2on"
api_secret = "R6GLsHrRx60U6bMrGaoEyD8RgSMqGQn4woeYkCmmLmtDrV4FQS"
access_token_key = "171599591-yAOxqWgwAJnF1NJNYy68pGLHlE9IRKFzGFVmFL4T"
access_token_secret = "bkpD7WeKFnyXhgPRLH0IpAQwOODr6yhzz4pBeOL8VP5P7"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  # url = "https://api.twitter.com/1.1/search/tweets.json?q=microsoft"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

def fetchTweetText():
  url = "https://stream.twitter.com/1.1/statuses/sample.json?language=en"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    try:
      print json.loads(line.strip())['text'].replace('\n', ' ').encode('utf-8')
    except KeyError:
      pass

if __name__ == '__main__':
  fetchsamples()
  # fetchTweetText()
