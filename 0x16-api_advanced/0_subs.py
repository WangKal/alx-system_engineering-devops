#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers from the Reddit API"""
    try:
        r = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers={'User-agent': 'my-app-name/0.1 by u/Feisty_Corgi_822'},
            allow_redirects=False
        )
        
        # Check if the request was successful
        if r.status_code != 200:
            print("Error: Received status code {}".format(r.status_code))
            return 0

        # Parse the JSON response
        json = r.json()
        data = json.get('data')
        
        # Check if the 'data' field is present
        if data is None:
            print("Error: 'data' field is missing from the response")
            return 0

        # Return the number of subscribers
        return data.get('subscribers', 0)
    
    except requests.exceptions.RequestException as e:
        # Handle connection errors or any issues with the request
        print("Request Exception: {}".format(e))
        return 0
    except ValueError as e:
        # Handle issues with parsing JSON
        print("JSON Parse Error: {}".format(e))
        return 0
    except Exception as e:
        # Catch any other errors
        print("An unexpected error occurred: {}".format(e))
        return 0

