import requests
import csv
import os


def fetch_data_from_api(api_url="http://localhost:5050/api/fitness_data"):
    """
    Fetch JSON data from the given API endpoint.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Received status code {response.status_code}")
        return []


def store_data_csv(data, filename="fitness_data.csv"):
    """
    Store the fetched JSON data in a csv file
    """
    if not data:
        print("No data to store.")
        return

    # Get all field names from the first record
    field_names = data[0].keys()

    # Check if file already exists
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        # If the file doesn't exist yet, write a header colulm
        if not file_exists:
            writer.writeheader()

        # Write each data record
        for record in data:
            writer.writerow(record)

    print(f"Data successfully stored in {filename}.")


if __name__ == "__main__":
    # Fetch data from the simulated API
    fitness_data = fetch_data_from_api("http://localhost:5050/api/fitness_data")

    # Store the data in a CSV
    store_data_csv(fitness_data, "fitness_data.csv")

