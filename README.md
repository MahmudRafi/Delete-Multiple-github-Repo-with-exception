# GitHub Repository Deletion Script

This Python script allows you to delete multiple repositories from your GitHub account based on a provided list of repositories to keep. Be cautious while using this script, as it will permanently delete repositories from your GitHub account.

![Telegram Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/240px-Telegram_logo.svg.png)

For any questions or help, you can contact me on Telegram: [t.me/mahmud_rafi](https://t.me/mahmud_rafi)

## Instructions

1. **Create a GitHub Personal Access Token:**
   - Go to the [GitHub settings page](https://github.com/settings/profile).
   - Click on "Developer settings" in the left sidebar.
   - From the developer settings page, click on "Personal access tokens."
   - Click on "Generate new token."
   - Enter your GitHub password if prompted.
   - Give the token a meaningful name and select the appropriate scopes (permissions) based on what you need your script to do. For this script, you'll need at least "delete_repo" permission.
   - Click on "Generate token."
   - **IMPORTANT:** Copy the generated access token and save it in a safe place. Once you leave the page, you won't be able to see the token again.

2. **Install PyGithub:**
   - To interact with the GitHub API from Python, you'll need to install the PyGithub library. You can install it using pip:
     ```
     pip install PyGithub
     ```

3. **Create the Python Script:**
   - Open a text editor (e.g., Notepad, VSCode, Sublime Text) and create a new file.
   - Copy and paste the following code into the file:

```python
from github import Github

def delete_repositories(username, access_token, repos_to_keep):
    # Create a GitHub instance using the access token
    g = Github(access_token)
    user = g.get_user(username)
    
    # Get all repositories of the user
    repos = user.get_repos()

    # Loop through each repository and check if it should be deleted
    for repo in repos:
        if repo.name not in repos_to_keep:
            # Delete the repository
            repo.delete()
            print(f"Deleted repository: {repo.name}")

if __name__ == "__main__":
    # Replace "your_github_username" with your actual GitHub username
    username = "your_github_username"
    
    # Replace "YOUR_ACCESS_TOKEN" with the access token you generated
    access_token = "YOUR_ACCESS_TOKEN"
    
    # List the names of repositories you want to keep
    repos_to_keep = ["Repo1", "Repo2", "Repo3"]
    
    # Call the function to delete the unwanted repositories
    delete_repositories(username, access_token, repos_to_keep)
