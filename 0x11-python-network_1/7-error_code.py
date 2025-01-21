#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    response = requests.get(argv[1])
    status = response.status_code
    print(response.text) if status < 400 else print(
            "Error code: {}".format(r.status_code))
