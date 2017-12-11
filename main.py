"""
A lot of the functions used in this file are going to
be from the Yelp Fusion API sample python code.
I contributed to it but definitely did not do most of the work.

This program requires the Python requests library, which can be installed via:
'pip install -r rquirements.txt'

Sample usage of this program:
'python sample.py --location="Anaheim, CA"'
"""

import argparse
import json
import pprint
import urllib
import requests
import ConfigParser
import os
from urllib2 import HTTPError
from urllib import quote

# Fetching data from the config file
config = ConfigParser.RawConfigParser()

config.read('app_data.cfg') # change this file to be your own config file
                            # in the repo the config file is called 'sample.cfg'

# Setting up the API key from config file
API_KEY = config.get('YELP', 'API_KEY')

# Yelp API constants, you shouldn't have the change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/' # Business ID will come after slash.

# Defaults for the app
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Fullerton, CA'

def main():
    #If the program works properly, you should see the API Key printed to the screen
    print (API_KEY)

main()
