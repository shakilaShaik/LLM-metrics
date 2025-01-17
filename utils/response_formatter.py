def build_json_output(data, default_start_date, default_end_date):
    """
    Constructs the JSON output based on extracted data and defaults.
    """
    results = []
    for entry in data:
        entity = entry.get("Entity", "Unknown Company")
        parameter = entry.get("Parameter", "Unknown Metric")
        start_date = entry.get("Start Date", default_start_date)
        end_date = entry.get("End Date", default_end_date)

        results.append({
            "Entity": entity,
            "Parameter": parameter,
            "Start Date": start_date,
            "End Date": end_date
        })
    return results
