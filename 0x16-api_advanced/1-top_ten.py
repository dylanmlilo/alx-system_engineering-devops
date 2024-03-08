#!/usr/bin/python3
""" prints hot posts on a given Reddit subreddit """
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for post in response.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
