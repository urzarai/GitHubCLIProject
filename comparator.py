from rich.table import Table
from rich.console import Console

console = Console()

def compare_users(user1, user2, user1_starred, user2_starred):
    console.rule("[bold blue]GitHub User Comparison")

    table = Table(title="GitHub Profile Comparison", show_lines=True)
    table.add_column("Metric", style="bold yellow")
    table.add_column(user1["login"], style="bold magenta")
    table.add_column(user2["login"], style="bold cyan")

    metrics = {
        "Name": ("name", "N/A"),
        "Public Repos": ("public_repos", 0),
        "Followers": ("followers", 0),
        "Following": ("following", 0),
        "Starred Repos": (None, 0)  # Special case for starred repos
    }

    for label, (key, default) in metrics.items():
        if label == "Starred Repos":
            val1 = len(user1_starred) if user1_starred else 0
            val2 = len(user2_starred) if user2_starred else 0
        else:
            val1 = user1.get(key, default)
            val2 = user2.get(key, default)
        table.add_row(label, str(val1), str(val2))

    console.print(table)
