import os
import requests
from dotenv import load_dotenv
import urllib3
import plotly.express as px

# Suppress only the single InsecureRequestWarning from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

proxy_username = os.getenv('PROXY_USERNAME')
proxy_password = os.getenv('PROXY_PASSWORD')
proxy_host = os.getenv('PROXY_HOST')
proxy_port = os.getenv('PROXY_PORT')

proxy_string = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"

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

# Process the response into a dictionary.
response_dicts = r.json()
print(f"Total repositories: {response_dicts['total_count']}")

# Process the repositories.
repo_dicts = response_dicts['items']
repo_names, stars, hover_texts, repo_links = [], [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    
    stars.append(repo_dict['stargazers_count'])
    
    hover_text = f"{repo_dict['owner']['login']}<br />{repo_dict['description']}"
    hover_texts.append(hover_text)
    
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}' target='_blank'>{repo_url}</a>"
    repo_links.append(repo_link)

# Make a bar chart of the repositories.
fig = px.bar(
    x = repo_links,
    y = stars,
    labels={'x' : 'Repository Names', 'y' : 'Stars'},
    title='Top Python Repositories on GitHub (Stars > 10,000)',
    hover_name=hover_texts
)

fig.update_layout(
    title_font_size=24,
    xaxis_title_font_size=18,
    yaxis_title_font_size=18,
)

fig.update_traces(marker_color='blue', texttemplate='%{y}', textposition='outside')

fig.show()