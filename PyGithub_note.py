#pip inxtall PyGithub

from github import Github

# First create a Github instance using an access token
g = Github("your_access_token")

# Get user information
user = g.get_user()
print(user.login)

# Creating a New Repository
user = g.get_user()
repo = user.create_repo(name="new-repo", description="This is your new repo", private=False)


# Creating an Issue
repo = g.get_repo("owner/repo")
issue = repo.create_issue(title="Issue title", body="Issue description")
