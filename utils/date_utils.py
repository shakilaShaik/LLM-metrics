from datetime import datetime, timedelta

def parse_relative_date(date_str):
    """
    Converts relative date strings (e.g., "last year", "Q3 2023") into ISO 8601 format.
    """
    today = datetime.today()
    if "last year" in date_str.lower():
        return (today.replace(year=today.year - 1, month=1, day=1).strftime("%Y-%m-%d"),
                today.replace(year=today.year - 1, month=12, day=31).strftime("%Y-%m-%d"))
    elif "last quarter" in date_str.lower():
        quarter = (today.month - 1) // 3
        start_month = (quarter - 1) * 3 + 1
        end_month = start_month + 2
        start_date = today.replace(month=start_month, day=1)
        end_date = (start_date + timedelta(days=89)).replace(day=1) - timedelta(days=1)
        return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
    return None, None
