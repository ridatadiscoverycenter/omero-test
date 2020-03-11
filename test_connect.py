import os
from connect import connection_test

USERNAME = os.environ['OMERO_USERNAME']
PASSWORD = os.environ['OMERO_PASSWORD']
HOSTNAME = os.environ.get('hostname', 'pricaimcit.services.brown.edu')

def test_secure_connect():
    connection_test(USERNAME, PASSWORD, host=HOSTNAME, port=4064, secure=True)

def test_insecure_connect():
    connection_test(USERNAME, PASSWORD, host=HOSTNAME, port=4063, secure=False)
