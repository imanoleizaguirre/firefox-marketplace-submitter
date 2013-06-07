Firefox Marketplace Submitter
=============================

A collection of random experiments with
[Firefox Marketplace API](https://firefox-marketplace-api.readthedocs.org/en/latest/).

Some of them require Persona authentication, which isn't included yet in
this project.

As they are only experiments, they shouldn't be used in production.

Some libraries are required for using this methods, included in the
requeriments file, you can install them with [pip](https://pypi.python.org/pypi/pip):
* [Requests](http://docs.python-requests.org/en/latest/)


Some previous knowledgement about how Firefox Marketplace works is strongly
recommended. You can take a look at the
[official documentation](https://marketplace.firefox.com/developers/) first.

Examples
---------

A couple of basic examples are provided to test the submission system.
One of them contains valid required files, while the other contains exactly the
same, but an invalid manifest file.

Validation
-----------
There are two ways of validating an application, one per each application type:
Packaged application validation and manifest validation.

**Packaged Application Validation**

Validator for packaged application. The full package is sent to the validator
and the API returns a response. If everything is valid, the response provides
an identificator needed in the submission process.

These applications are hosted by the Marketplace.

**Manifest Validation**

Users can deploy their application on their own servers, and send just the
manifest's url itself to the Marketplace for the validation. The Marketplace
validator will search for all the requeriments there.

Submission
------------
Requires Persona authentication, so it's still in development. Currently the
Firefox Marketplace's API has a restriction of 10 submissions per day.