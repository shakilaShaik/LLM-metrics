import openai
from config.settings import OPENAI_API_BASE, OPENAI_API_KEY

# Configure OpenAI API
openai.api_base = OPENAI_API_BASE
openai.api_key = OPENAI_API_KEY

def query_llm(query):
    """
    Query the LLM API with the user's input and return the raw response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a query analyzer for company performance metrics. "
                        "Analyze the user's query and return ONLY a valid JSON response with the following format:\n"
                        "{\n"
                        "  'companies': [\n"
                        "    {\n"
                        "      'name': '<company_name>',\n"
                        "      'metric': '<performance_metric>',\n"
                        "      'start_date': '<ISO_start_date>',\n"
                        "      'end_date': '<ISO_end_date>'\n"
                        "    }\n"
                        "  ]\n"
                        "}\n"
                        "Do not include any extra text or explanation."
                    )
                },
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error querying the LLM: {e}")
        return None
