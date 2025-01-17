from config.settings import get_default_dates
from llm.query_handler import parse_query_with_llm
from utils.date_utils import parse_relative_date
from utils.response_formatter import build_json_output

def handle_user_query(query):
    """
    Processes the user query and returns the JSON response.
    """
    default_start_date, default_end_date = get_default_dates()
    llm_response = parse_query_with_llm(query)

    if llm_response is None or not llm_response:
        return {"error": "Failed to parse query. Please provide a valid query."}

    return build_json_output(llm_response, default_start_date, default_end_date)

if __name__ == "__main__":
    print("LLM-Powered Metrics Query Application")
    while True:
        user_query = input("\nEnter your query (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            break
        result = handle_user_query(user_query)
        print("\nGenerated JSON Response:\n", result)
