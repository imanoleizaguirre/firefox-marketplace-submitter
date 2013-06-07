import requests
import json

from configuration import login_url


def login():
    """
    Authenticates in Firefox Marketplace
    """
    payload = {"assertion": "user@domain.com",
               "audience": "https://mydomain.com:80"}
    headers = {'content-type': 'application/json'}

    r = requests.post(login_url,
                      data=json.dumps(payload),
                      headers=headers)

    print "response code: %s" % r.status_code

    #response = json.loads(r.text)
    #print response


login()
