import os
from managezoho import get_deals, refresh_access_token
from time import sleep
from createtrello import set_api_key

if __name__ == "__main__":
    
    #initialising tokens and keys from environment variables
    try:
        ZOHO_CLIENT_ID = os.environ["ZOHO_CLIENT_ID"]
        ZOHO_CLIENT_SECRET = os.environ["ZOHO_CLIENT_SECRET"]
        ZOHO_REFRESH_TOKEN = os.environ["ZOHO_REFRESH_TOKEN"]
        TRELLO_API_KEY = os.environ["TRELLO_API_KEY"]
        TRELLO_API_TOKEN = os.environ["TRELLO_API_TOKEN"]
    except KeyError as e:
        print(f"Missing environment variable: {e}")
        exit(1)  # Exit the program if a required variable is missing

    ZOHO_ACCESS_TOKEN = ""
    
    # Fetch the access token using the refresh token function
    ZOHO_ACCESS_TOKEN = refresh_access_token(ZOHO_REFRESH_TOKEN, ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET)
    
    # Set the Trello API key and token
    set_api_key(TRELLO_API_KEY, TRELLO_API_TOKEN)
   
    while True:
        # Fetch new deals from Zoho CRM
        # If the access token expires, refresh it
        if get_deals(ZOHO_ACCESS_TOKEN) == "401":
            print("Access token expired, refreshing...")
            ZOHO_ACCESS_TOKEN = refresh_access_token(ZOHO_REFRESH_TOKEN, ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET)
            continue
        sleep(30)