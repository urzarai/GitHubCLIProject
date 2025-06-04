from rich.console import Console
from rich.table import Table
from collections import defaultdict
from util import format_date

console = Console()

def display_user_overview(user_data, repos, starred):
    table = Table(title=f"{user_data['login']}'s GitHub Profile", show_lines=True)

    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Name", user_data.get("name", "N/A"))
    table.add_row("Public Repos", str(user_data.get("public_repos", 0)))
    table.add_row("Followers", str(user_data.get("followers", 0)))
    table.add_row("Following", str(user_data.get("following", 0)))
    table.add_row("Starred Repos", str(len(starred)))

    console.print(table)

def display_repo_commits(events):
    """Display recent push event commits from user's public activity"""
    repo_commits = defaultdict(list)

    for event in events:
        if event["type"] == "PushEvent":
            repo_name = event["repo"]["name"]
            for commit in event["payload"]["commits"]:
                message = commit.get("message", "No message")
                timestamp = format_date(event["created_at"])
                repo_commits[repo_name].append((message, timestamp))

    if not repo_commits:
        console.print("\n[bold yellow]No recent commits found.[/bold yellow]")
        return

    for repo, commits in repo_commits.items():
        console.rule(f"[bold green]{repo} - Recent Commits")
        for msg, time in commits:
            console.print(f"[blue]{msg}[/blue] [dim]({time})[/dim]")
