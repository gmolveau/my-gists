import os

import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.environ["GITHUB_USERNAME"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

def fetch_all_gists(username, token):
    gists = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/gists?page={page}&per_page=100"
        headers = {
            'Authorization': f'token {token}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch gists: {response.status_code}")
            break

        page_gists = response.json()
        if not page_gists:
            break

        gists.extend(page_gists)
        page += 1

    return gists

def create_markdown_file(gists, filename="gists.md"):
    with open(filename, 'w') as f:
        f.write(f"# List of my public [gists](https://gist.github.com/{GITHUB_USERNAME})\n\n")
        for gist in gists:
            if gist['public']:
                description = gist['description'] if gist['description'] else "No description"
                gist_url = gist['html_url']
                f.write(f"- [{description}]({gist_url})\n")

def main():
    gists = fetch_all_gists(GITHUB_USERNAME, GITHUB_TOKEN)
    create_markdown_file(gists, "README.md")

if __name__ == "__main__":
    main()
