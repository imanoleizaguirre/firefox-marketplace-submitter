import requests
import json
import base64

from configuration import api_url, validation_url, max_retries


def validate_manfest(manifest_url):
    """
    Validates a Firefox Marketplace Manifest. Doesn't require authentication.
    """

    payload = {'manifest': manifest_url}
    headers = {'content-type': 'application/json'}

    r = requests.post(validation_url,
                      data=json.dumps(payload),
                      headers=headers)

    return validate_response(r, 0)


def validate_packaged_app():
    """
    Validates a packaged application
    """
    file = open('examples/game.zip', "rb")
    data = file.read()
    file.close()
    file_data = base64.b64encode(data)

    payload = {"upload": {"type": "application/zip",
                          "data": file_data,
                          "name": "game.zip"}}
    headers = {'content-type': 'application/json'}

    r = requests.post(validation_url,
                      data=json.dumps(payload),
                      headers=headers)

    return validate_response(r, 0)


def is_processed(r):
    """
    Check if a validation try has been processed by the Marketplace
    """
    if r.status_code == 201 or r.status_code == 200:
        response = json.loads(r.text)
        processed = response.get("processed")
    else:
        processed = False
        print "\tError contacting the Marketplace"

    return processed


def validate_response(r, retries):
    """
    Reads and processes the response from the Marketplace
    """
    response = json.loads(r.text)
    #print response

    if is_processed(r):
        print "\tValidation processed"
        return process_response(response)
    else:
        print "\tValidation queued"
        return fetch_validation(response, retries)


def process_response(response):
    """
    Reads a processed response
    """
    validation = response.get("validation")

    print "\t%s errors and %s warnings:\n" % (validation.get("errors"),
                                               validation.get("warnings"))

    print_error_message(validation.get("messages"))

    if response.get("valid"):
        print "Upload Id: %s" % response.get("id")
        return response.get("id"), True
    else:
        return None, False


def fetch_validation(response, retries):
    """
    Tries to fetch the Marketplace's response from a queued query
    """
    processed = False
    retried_response = False
    while (retries < max_retries and not processed):
        retries += 1
        url = api_url % response.get("resource_uri")
        print "\tRetry validation %s %s" % (retries, url)
        r = requests.get(url)
        processed = is_processed(r)

        if (processed):
            retried_response = validate_response(r, retries)

    return retried_response


def print_error_message(messages):
    """
    Prints error message
    """
    if messages:
        for msg in messages:
            print "\t\t%s: %s" % (msg.get("type"), msg.get("message"))
            print "\t\t%s" % str(msg.get("description"))
            print
