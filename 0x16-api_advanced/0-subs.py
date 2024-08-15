#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """return total subscribers of reddit's subreddit"""

    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    try:
        response = requests.get(url,
                                headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'},
                                allow_redirects=False).json()
        return response['data'].get('subscribers')
    except:
        return 0
