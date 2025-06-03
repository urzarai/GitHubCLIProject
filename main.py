import argparse 
from github_api import (
    get_user_data,
    get_user_repos,
    get_starred_repos
)
from ui_renderer import display_user_overview
from comparator import compare_users

def main():
    parser = argparse.ArgumentParser(description="GitHub CLI Viewer")
    parser.add_argument("username", help="GitHub username to inspect")
    parser.add_argument("--compare", help="GitHub username to compare against", default=None)

    args = parser.parse_args()

    if not args.compare:
        # Fetch data for the primary user only
        user1_data = get_user_data(args.username)
        user1_repos = get_user_repos(args.username)
        user1_starred = get_starred_repos(args.username)
        # Display single user info
        display_user_overview(user1_data, user1_repos, user1_starred)
    else:
        # Fetch data for both users and compare
        user1_data = get_user_data(args.username)
        user1_starred = get_starred_repos(args.username)
        
        user2_data = get_user_data(args.compare)
        user2_starred = get_starred_repos(args.compare)

        print("\n[Comparing Profiles]\n")
        compare_users(user1_data, user2_data, user1_starred, user2_starred)

if __name__ == "__main__":
    main()
