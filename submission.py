import requests
import json

from configuration import submission_url


def submit_packaged_app(assertion, upload_id):
    """
    Submits a packaged app to the Marketplace. Requires authentication.
    """

    print "Submitting application: %s" % upload_id

    payload = {"upload": upload_id}
    headers = {'content-type': 'application/json'}

    r = requests.post(submission_url,
                      data=json.dumps(payload),
                      headers=headers)

    print "response code: %s" % r.status_code

    if r.status_code == 200:
        return True
    else:
        return False
