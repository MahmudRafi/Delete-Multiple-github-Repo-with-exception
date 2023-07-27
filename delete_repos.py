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
