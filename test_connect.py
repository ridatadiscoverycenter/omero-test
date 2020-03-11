import os
from connect import connection_test

USERNAME = os.environ['OMERO_USERNAME']
PASSWORD = os.environ['OMERO_PASSWORD']
HOSTNAME = os.environ.get('hostname', 'pricaimcit.services.brown.edu')

def test_secure_connect():
    '''Connect on secure port should work'''
    assert connection_test(USERNAME, PASSWORD, host=HOSTNAME, port=4064, secure=True)

def test_insecure_on_secure_port():
    '''Insecure connection on a secure port should not work'''
    assert not connection_test(USERNAME, PASSWORD, host=HOSTNAME, port=4064, secure=False)

def test_insecure_connect():
    '''Insecure connections should not work'''
    assert not connection_test(USERNAME, PASSWORD, host=HOSTNAME, port=4063, secure=False)

def test_secure_on_insecure_port():
    '''Secure connections on an insecure port should not work'''
    assert not connection_test(USERNAME, PASSWORD, host=HOSTNAME, port=4063, secure=True)

