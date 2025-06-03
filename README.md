# GitHubCLIProject

Fetch details of user using GitHub API

## Installation

1. Open PowerShell as Administrator
2. Go to the directory where you have your code for this project
    ```powerShell
    cd <directory address>
3. Type the following commands in the powerShell terminal:
    ```powerShell
    python -m pip install --upgrade pip
    ```powerShell
    pip install requests rich python-dotenv

## Features

- View detailed information about a single GitHub user
- Compare two GitHub users side-by-side on key metrics
- Displays metrics including Name, Public Repos, Followers, Following, and Starred Repos
- Clean, easy-to-read terminal output with tables powered by Rich library


## How to View Individual User Details

To fetch and display details of a single GitHub user, run:

    ```powerShell
    python main.py <username>
    ```

## Compare Details of two users

To fetch, display and compare details of two single GitHub users, run:

```powerShell
python main.py <username1> --compare <username2>