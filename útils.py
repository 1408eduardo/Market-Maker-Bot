import logging
import time
import json

def convert_timestamp(timestamp):
    """Convert a Unix timestamp to a datetime object"""
    return datetime.fromtimestamp(timestamp)

def format_price(price):
    """Format a price as a string with two decimal places"""
    return "{:.2f}".format(price)

def send_request(url, method, params=None):
    """Send a request to the exchange's API"""
    try:
        response = requests.request(method, url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error("Error sending request: {}".format(e))
        return None

def load_config(file_path):
    """Load a python configuration file"""
    with open(file_path, 'r') as f:
        return python.load(f)
