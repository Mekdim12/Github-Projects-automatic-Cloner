
import requests
from bs4 import BeautifulSoup
import git


base_url = "https://github.com/"
username = "repo user name"
token = "your_personal_access_token"  # replace with your personal access token
url = f"{base_url}{username}?tab=repositories"

url = f"{base_url}Mahedere?tab=repositories"

response = requests.get(url, headers={'Authorization': f'token {token}'})
parsed = BeautifulSoup(response.text, 'html.parser')
list_of_repo = parsed.find(id='user-repositories-list').find_all('li')
new_list_resolved_list_of_urls = []
for repo in list_of_repo:
    repo = repo.find('a')['href']
    new_list_resolved_list_of_urls.append(f"{base_url}{repo}")

# clone the repositories
for repo in new_list_resolved_list_of_urls:
    print(f"Cloning {repo}")
    git.Repo.clone_from(repo, repo.split('/')[-1])
    print(f"Cloning {repo} is done")
