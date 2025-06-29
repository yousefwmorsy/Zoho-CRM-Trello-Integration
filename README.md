# Integration: ZOHO CRM + Trello
Automatically creates and configures Trello project boards when new implementation projects that are in the "Project Kickoff" stage are added/modified in the Zoho CRM. Each board is linked back to the Zoho CRM record.

## Setup Steps

1. **Clone or Download the Repository**
   - Place all files in a working directory on your machine.

2. **Create a Python Virtual Environment**
   - Open PowerShell in the project directory.
   - Create a virtual environment:
     ```powershell
     python -m venv venv
     ```

3. **Set Environment Variables and Activate the Virtual Environment**
   - Edit `Activate.ps1` and set the following variables:
     - `ZOHO_CLIENT_ID`
     - `ZOHO_CLIENT_SECRET`
     - `ZOHO_REFRESH_TOKEN`
     - `TRELLO_API_KEY`
     - `TRELLO_API_TOKEN`

    By running the following command:
    ```powershell
    $env:ZOHO_CLIENT_ID = "your_zoho_client_id"
    $env:ZOHO_CLIENT_SECRET = "your_zoho_client_secret"
    $env:ZOHO_REFRESH_TOKEN = "your_zoho_refresh_token"
    $env:TRELLO_API_KEY = "your_trello_api_key"
    $env:TRELLO_API_TOKEN = "your_trello_api_token"
    ```

    - Activate the environment:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

4. **Install Required Python Packages**
   - Install dependencies:
     ```powershell
     pip install requests
     ```

## How to Run the Script

1. Make sure your virtual environment is activated in PowerShell.
2. Run the main script:
   ```powershell
   python main.py
   ```

## Notes

- The script expects valid Zoho and Trello API credentials. If any environment variable is missing, the script will exit with an error.
- The script runs in an infinite loop, polling Zoho CRM every 30 seconds (can be updated in `main.py`). Stop it with `Ctrl+C`.
- For any issues with API limits or authentication, check the printed error messages for details.
- These setup details are for a windows environment, linux environments may have some different steps.
