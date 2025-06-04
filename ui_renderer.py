from rich.console import Console
from rich.table import Table

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
