#!/usr/bin/env python
import argparse
import logging

import omero.clients
from omero.gateway import BlitzGateway

HOST = 'tcp://pricaimcit.services.brown.edu'
PORT = 4063

def connection_test(username, password, host=HOST, port=PORT, secure=False):
    print(f'connecting to {host}:{port} secure={secure}')
    conn = BlitzGateway(username, password, host=host, port=port, secure=False)
    try:
        conn.connect()
        conn.close()
        return True
    except:
        return False

def main():
    logger = logging.getLogger('omero.gateway')
    logger.setLevel(logging.DEBUG)
    logger = logging.getLogger('omero.clients')
    logger.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser(description='Test connection to omero') 
    parser.add_argument('-H', '--host', default=HOST, required=False)
    parser.add_argument('-p', '--port', default=PORT, required=False) 
    parser.add_argument('-s', '--secure', action='store_true', required=False)
    parser.add_argument('username')
    parser.add_argument('password')

    args = parser.parse_args()

    assert connection_test(args.username, args.password, args.host, args.port, args.secure)

if __name__ == '__main__':
    main()
