#!/usr/bin/python3
"""Module that consumes the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """Returns the number of SUBSCRIBERS
    If not a valid subreddit, return 0.

    Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
    """
    base_url = 'https://www.reddit.com/r/'

    url = '{}{}/about.json'.format(base_url, subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    results = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0
