import os
import requests
import base64
import re

# GitHub credentials
GITHUB_USERNAME = "rishabhgokhe"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Validate Token
if not GITHUB_TOKEN:
    print("❌ ERROR: GitHub token is missing. Set the TOKEN environment variable.")
    exit(1)

# List of repositories
REPOS = ["Dialytics", "README-Sync", "birthday-wisher"]

# Centralized blocks directory
BLOCKS = ["connect-with-me.md", "about-me.md", "contribution-guidelines.md", "license.md"]

# Read blocks content
block_data = {}
for block in BLOCKS:
    if os.path.exists(block):
        with open(block, "r") as f:
            block_data[block] = f.read().strip()
    else:
        print(f"⚠️ WARNING: {block} not found. Skipping...")

# GitHub API Headers
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to update README content dynamically
def update_readme_content(old_content):
    new_content = old_content
    for block, content in block_data.items():
        start_marker = f"<!-- {block}-start -->"
        end_marker = f"<!-- {block}-end -->"

        pattern = re.compile(rf"{start_marker}.*?{end_marker}", re.DOTALL)
        if pattern.search(old_content):
            new_content = pattern.sub(f"{start_marker}\n{content}\n{end_marker}", new_content)
    return new_content

# Update README in all repos
for repo in REPOS:
    print(f"\n🚀 Updating README for {repo}...")

    # Fetch README from GitHub
    repo_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo}/contents/README.md"
    response = requests.get(repo_url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to fetch README for {repo}: {response.json().get('message', 'Unknown error')}")
        continue

    readme_data = response.json()
    old_readme_content = base64.b64decode(readme_data["content"]).decode("utf-8")
    sha = readme_data["sha"]

    # Process README content
    new_readme_content = update_readme_content(old_readme_content)

    if old_readme_content == new_readme_content:
        print("⚠️ No changes detected in README. Skipping update.")
        continue

    # Encode new README content in Base64
    encoded_content = base64.b64encode(new_readme_content.encode("utf-8")).decode("utf-8")

    # Update README via GitHub API
    update_data = {
        "message": "Updated README with latest blocks",
        "content": encoded_content,
        "sha": sha
    }

    update_response = requests.put(repo_url, headers=headers, json=update_data)

    if update_response.status_code == 200:
        print(f"✅ Successfully updated README for {repo}")
    else:
        print(f"❌ Failed to update README for {repo}: {update_response.json().get('message', 'Unknown error')}")