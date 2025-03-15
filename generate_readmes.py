import os
import requests

# List of your GitHub repositories
REPOS = [
    "birthday-wisher",
] 

# GitHub username & personal access token
GITHUB_USERNAME = "rishabhgokhe"
GITHUB_TOKEN = os.getenv("TOKEN")

# Centralized blocks directory
BLOCKS = ["about-me.md"]

# Fetch block contents
block_data = {}
for block in BLOCKS:
    with open(block, "r") as f:
        block_data[block] = f.read()

# Update README in all repos
for repo in REPOS:
    readme_path = f"./{repo}/README.md"

    if not os.path.exists(readme_path):
        print(f"Skipping {repo}, README.md not found.")
        continue

    # Read existing README
    with open(readme_path, "r") as f:
        readme_content = f.read()

    # Replace blocks dynamically
    for block, content in block_data.items():
        start_marker = f"<!-- {block}-start -->"
        end_marker = f"<!-- {block}-end -->"

        if start_marker in readme_content and end_marker in readme_content:
            readme_content = readme_content.split(start_marker)[0] + \
                             start_marker + "\n" + content + "\n" + end_marker + \
                             readme_content.split(end_marker)[1]

    # Write updated README
    with open(readme_path, "w") as f:
        f.write(readme_content)

    # Push changes to GitHub
    repo_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo}/contents/README.md"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(repo_url, headers=headers).json()
    sha = response.get("sha", "")

    data = {
        "message": "Updated README with latest blocks",
        "content": readme_content.encode("utf-8").decode("latin1"),
        "sha": sha
    }

    requests.put(repo_url, headers=headers, json=data)

print("All READMEs updated successfully!")
