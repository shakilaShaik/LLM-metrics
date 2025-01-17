from openai import OpenAI

client = OpenAI(api_key="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")
import json

def parse_query_with_llm(query):
    """
    Sends the user query to the LLM and extracts relevant information.
    """
      # Set your API key here
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",  # Replace with the correct model name
        messages=[
            {"role": "system", "content": "You are an assistant that extracts structured data from user queries."},
            {"role": "user", "content": query}
        ],
        max_tokens=200)
        response_text = response.choices[0].message.content
        data = json.loads(response_text)
        return data
    except Exception as e:
        print("Error querying the LLM:", e)
        return None
