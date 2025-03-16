import os
import requests
import base64

# GitHub credentials
GITHUB_USERNAME = "rishabhgokhe"
GITHUB_TOKEN = os.getenv("TOKEN")

# List of repositories
REPOS = ["Dialytics, README-Sync, birthday-wisher"]

# Centralized blocks directory
BLOCKS = ["connect-with-me.md", "about-me.md", "contribution-guidelines.md", "license.md"]

# Read blocks content
block_data = {}
for block in BLOCKS:
    with open(block, "r") as f:
        block_data[block] = f.read()

# Update README in all repos
for repo in REPOS:
    print(f"Updating README for {repo}...")

    # Fetch README from GitHub
    repo_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo}/contents/README.md"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

    response = requests.get(repo_url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Failed to fetch README for {repo}: {response.json()}")
        continue

    readme_data = response.json()
    old_readme_content = base64.b64decode(readme_data["content"]).decode("utf-8")
    sha = readme_data["sha"]

    # Replace blocks dynamically
    new_readme_content = old_readme_content
    for block, content in block_data.items():
        start_marker = f"<!-- {block}-start -->"
        end_marker = f"<!-- {block}-end -->"

        if start_marker in old_readme_content and end_marker in old_readme_content:
            new_readme_content = old_readme_content.split(start_marker)[0] + \
                                 start_marker + "\n" + content + "\n" + end_marker + \
                                 old_readme_content.split(end_marker)[1]

    # Debug: Show before & after content
    print("\n🔍 OLD README CONTENT:\n", old_readme_content[:500])  # Show first 500 chars
    print("\n🆕 NEW README CONTENT:\n", new_readme_content[:500])  # Show first 500 chars

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
        print(f"❌ Failed to update README for {repo}: {update_response.json()}")