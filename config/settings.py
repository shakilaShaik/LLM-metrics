from datetime import datetime, timedelta

# Groq LLM API Configuration
LLM_API_KEY = "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"
LLM_MODEL = "llama-3.1-8b-instant"

def get_default_dates():
    """
    Returns default start and end dates in ISO 8601 format.
    Start Date: Today - 1 year
    End Date: Today
    """
    today = datetime.today()
    one_year_ago = today - timedelta(days=365)
    return one_year_ago.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")
