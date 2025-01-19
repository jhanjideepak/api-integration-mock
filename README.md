# API Integration Project

This project demonstrates a simple API integration using Python. It includes a mock API that simulates fitness data and a script to fetch and store this data in a CSV file.

## Project Structure

- **fetch_and_store.py**: This script fetches JSON data from the mock API and stores it in a CSV file. A python script fetching and storing the data
- **mock_api.py**: A Flask simulation that simulates fitness data for users.

## How to Run the Project

### Prerequisites

- Python 3.11
- Flask
- Requests
- numpy

### Setup

1. **Install the required packages**:
   ```bash
   pip install flask requests
   ```

2. **Run the Mock API**:
   - Navigate to the `api_integration` directory.
   - Start the Flask server by running:
     ```bash
     python mock_api.py
     ```
   - The server will start on `http://localhost:5050`.

3. **Fetch and Store Data**:
   - In a new terminal, navigate to the `api_integration` directory.
   - Run the data fetching script:
     ```bash
     python fetch_and_store.py
     ```
   - This will fetch data from the mock API and store it in `fitness_data.csv` in the current directory.

## Description

- The **mock API** simulates fitness data for 5 users ata time, generating random values for steps, heart rate, active minutes, calories consumed and blood pressure.
- The **fetch_and_store.py** script retrieves this data and appends it to a CSV file, creating the file if it doesn't exist.
