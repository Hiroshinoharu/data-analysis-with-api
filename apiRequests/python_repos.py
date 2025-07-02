import requests
import os
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress only the single InsecureRequestWarning from urllib3
urllib3.disable_warnings(InsecureRequestWarning)

load_dotenv()

proxy_username = os.getenv('PROXY_USERNAME')
proxy_password = os.getenv('PROXY_PASSWORD')
proxy_host = os.getenv('PROXY_HOST')
proxy_port = os.getenv('PROXY_PORT')

proxy_string = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"

# Set up the proxies dictionary.
proxies = {
    'http': proxy_string,
    'https': proxy_string
}

session = requests.Session()
session.trust_env = True  # Trust environment variables for proxies


# Make an API call and store the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {'Accept': 'application/vnd.github.v3+json'}
r = session.get(url, headers=headers, proxies=proxies, verify=False)
print(f"Status code: {r.status_code}")

# Converts the reoponse into a dictionary.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Repositories returned: {len(response_dict['items'])}")

# Examine the first repository.
repo_dicts = response_dict['items']

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository URL: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
    print(f"Created at: {repo_dict['created_at']}")
    print(f"Updated at: {repo_dict['updated_at']}")
    print(f"Language: {repo_dict['language']}")
    print(f"Forks count: {repo_dict['forks_count']}") 