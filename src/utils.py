from datetime import datetime
from typing import Optional


def get_year_and_month(from_ms: int):
    """Get the year and month from a given unix milliseconds timestamp.

    Args:
        from_ms (int): Unix milliseconds timestamp

    Returns:
        Tuple[int, int]: Year and month
    """

    # convert from_ms to a datetime object
    dt = datetime.fromtimestamp(from_ms / 1000)

    # extract year and month
    year = dt.year
    month = dt.month

    return year, month
