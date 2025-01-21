#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request and finally displays the body of the response
"""
import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    response = requests.post(argv[1], data=payload)
    print(response.text)
