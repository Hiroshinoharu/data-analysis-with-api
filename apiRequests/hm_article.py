import os
import requests
from dotenv import load_dotenv
import urllib3
import json

# Suppress insecurerequets warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set up environment variables
load_dotenv()

# Connect to the proxy
proxy_username = os.getenv('PROXY_USERNAME')
proxy_password = os.getenv('PROXY_PASSWORD')
proxy_host = os.getenv('PROXY_HOST')
proxy_port = os.getenv('PROXY_PORT')

proxy_string = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"

print(f"Using proxy: {proxy_string}")

proxies = {
    'http': proxy_string,
    'https': proxy_string
}

session =  requests.Session()
session.trust_env = True  # Trust environment variables for proxies

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

headers = {'Accept': 'application/json'}

r = session.get(url, headers=headers, proxies=proxies, verify=False)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a GET request to the API to get the submission information.
    submission_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    submission_r = session.get(submission_url, headers=headers, proxies=proxies, verify=False)
    submission_dict = submission_r.json()
    
    # Build a dictionary for each submission.
    submission_dict = {
        'title': submission_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': submission_dict.get('descendants', 0)  # Use .get() to avoid KeyError if 'descendants' is not present],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=lambda x: x['comments'], reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Comments: {submission_dict['comments']}")
    print(f"Link: {submission_dict['hn_link']}")