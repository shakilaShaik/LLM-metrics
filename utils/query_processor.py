import json
import datetime
from utils.llm_interface import query_llm

def parse_response(response, default_start_date, default_end_date):
    """
    Parse the JSON response from the LLM and format it.
    """
    try:
        # Convert the LLM response into a Python dictionary
        parsed_data = json.loads(response)
        results = []
        
        # Extract and format data
        for item in parsed_data.get("companies", []):
            results.append({
                "Entity": item.get("name", "Unknown"),
                "Parameter": item.get("metric", "Undefined"),
                "Start Date": item.get("start_date", default_start_date),
                "End Date": item.get("end_date", default_end_date)
            })
        return results
    except json.JSONDecodeError as e:
        print(f"Error parsing LLM response: {e}")
        print(f"Raw response: {response}")
        return {"error": "Invalid response format from LLM. Unable to parse data."}

def process_query(query):
    """
    Process the user's query by interacting with the LLM and parsing the response.
    """
    # Default date range
    today = datetime.date.today()
    default_start_date = (today - datetime.timedelta(days=365)).isoformat()
    default_end_date = today.isoformat()

    # Query the LLM
    llm_response = query_llm(query)
    if not llm_response:
        return {"error": "Failed to query the LLM. Please try again."}

    # Parse the response
    return parse_response(llm_response, default_start_date, default_end_date)
