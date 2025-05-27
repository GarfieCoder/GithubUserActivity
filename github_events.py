# Github User Activity Project for Roadmap.sh

# GitHub CLI api
# https://cli.github.com/manual/gh_api

# https://api.github.com/users/<username>/events


import json
import os
import requests

githubUserName = input("Enter GitHub username: ")
file_path = 'GitHubActviity.json'
userActivity = []

def fetch_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    event = response.json()
    latest_events = event  # Get the latest 10 events
    if response.status_code == 200:
        for event in latest_events:
            # Covering only the most common events
            if event['type'] == 'IssueCommentEvent':
                print(f"- :smiley: commented on issue {event['payload']['issue']['number']}")
            elif event['type'] == 'PushEvent':
                print(f"- :smiley: pushed to {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
                print(f"- :smiley: created issue {event['payload']['issue']['number']}")
            elif event['type'] == 'WatchEvent':
                print(f"- :smiley: starred {event['repo']['name']}")
            elif event['type'] == 'PullRequestEvent':
                print(f"- :smiley: created pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewEvent':
                print(f"- :smiley: reviewed pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f"- :smiley: commented on pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'CreateEvent':
                print(f"- :smiley: created {event['payload']['ref_type']} {event['payload']['ref']}")
            else:
                print(f"- :smiley: {event['type']}")
    else:
        print(f"Error fetching data for {username}: {response.status_code}")
        return []
    
fetch_user_activity(input("Enter GitHub username: "))



