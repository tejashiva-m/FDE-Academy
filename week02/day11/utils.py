from datetime import datetime


def format_date(iso_str: str | None) -> str:
    """Format an ISO timestamp like 2020-01-01T12:00:00Z into a readable string.

    Returns the original value if parsing fails or input is falsy.
    """
    if not iso_str:
        return "Unknown"
    try:
        # Handle trailing Z
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    except Exception:
        return iso_str
