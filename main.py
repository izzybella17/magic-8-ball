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
from flask import Flask

# Startings Flask App
app = Flask(__name__)

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
DEFAULT_LOCATION = 'Anaheim, CA'
SEARCH_LIMIT = 50


def request(host, path, api_key, url_params=None):
    """Given your API Key, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain
        api_key (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The Json response from the request.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print ((u'Querying {0} ...').format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, term, location):
    """Query the Search API by a search term and location.
    
    Args:
        term (str): The search term passed to the API.
        location (str): The searh location passed to the API.
    
    
    Returns:
        dict: The JSON response from the request.
    """
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)

def get_business(api_key, business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


def query_api(term, location):
    """Query the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the busines to query.
    """
    response = search(API_KEY, term, location)

    businesses = response.get('businesses')

    if not businesses:
        print (u'No businesses for {0} in {1} found.'.format(term, location))
        return
    
    for business in businesses:
        print (u'{0} - {1} - Rating: {2}').format(
                business['name'],
                business['price'],
                business['rating'])

    return businesses

#    business_id = businesses[0]['id']
#
#    print(u'{0} businesses found, querying business info ' \
#            'for the top result "{1}" ...'.format(
#                len(businesses), business_id))
#    response = get_business(API_KEY, business_id)
#
#    print(u'Result for business "{0}" found:'.format(business_id))
#    pprint.pprint(businesses, indent=2)


def main():
    #If the program works properly, you should see a business in Fullerton California
    query_api(DEFAULT_TERM, DEFAULT_LOCATION)

@app.route("/")
def hello():
    businesses = query_api(DEFAULT_TERM, DEFAULT_LOCATION)
    return businesses[0]['name']
    

if __name__ == '__main__':
    main()
