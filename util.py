from datetime import datetime

def format_date(iso_date_str):
    """Convert ISO 8601 date string to readable format."""
    try:
        date_obj = datetime.strptime(iso_date_str, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%Y-%m-%d %H:%M")
    except:
        return "Unknown"
