import requests
import os

GITHUB_API_URL = "https://api.github.com"

def get_user_data(username):
    url = f"{GITHUB_API_URL}/users/{username}"
    response = requests.get(url)
    return response.json()

def get_user_repos(username):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url)
    return response.json()

def get_user_events(username):
    url = f"{GITHUB_API_URL}/users/{username}/events"
    response = requests.get(url)
    return response.json()

def get_starred_repos(username):
    url = f"{GITHUB_API_URL}/users/{username}/starred"
    response = requests.get(url)
    return response.json()
