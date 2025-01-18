import json
from utils.query_processor import process_query

def main():
    """
    Main application loop to accept user queries and display formatted output.
    """
    print("LLM-Powered Metrics Query Application")
    print("Type 'exit' to quit the application.\n")

    while True:
        user_input = input("Enter your query: ").strip()
        if user_input.lower() == "exit":
            print("Thank you for using the application. Goodbye!")
            break

        # Process the query and display the results
        results = process_query(user_input)
        print("\nGenerated JSON Response:")
        print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
