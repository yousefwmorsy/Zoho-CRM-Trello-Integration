import requests
from createtrello import create_board

def update_board_id(id, zohoid, token):
    """
    Update the Zoho deal with the board ID.
    """

    url = f"https://www.zohoapis.com/crm/v2/Deals/{zohoid}"
    headers = {
        "Authorization": f"Zoho-oauthtoken {token}",
    }

    body = {
        "data": [
            {
                "Project_Board_ID_c": id
            }
        ]
    }

    response = requests.put(url, headers=headers, json=body)

    if response.status_code == 200:
        print(f"Successfully updated deal {zohoid}")
    else:
        print(f"Update failed ({response.status_code}):")
        print(response.text)
    

def get_deals(token):
    """
    Fetch deals from Zoho CRM and create Trello boards for new implementation projects that are in the project kickoff stage.
    """

    url = "https://www.zohoapis.com/crm/v2/Deals"
    headers = {
        "Authorization": f"Zoho-oauthtoken {token}",
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        for deal in data.get("data", []):
            print(f"Deal ID: {deal['id']}, Name: {deal['Deal_Name']}")
            # If the deal meets the criteria, create a board, then update the deal with the board ID
            if(deal["Stage"] == "Project Kickoff" and deal['Type'] == "New Implementation Project"):
                print(f"Creating board for deal: {deal['Deal_Name']}")
                # only create a board if it does not already have one
                if not deal['Project_Board_ID_c']:
                    board_id = create_board(deal['Deal_Name'])
                    update_board_id(board_id, deal['id'], token)
                else:
                    print(f"Deal {deal['id']} already has a board ID: {deal['Project_Board_ID_c']}")
    else:
        print(f"[Getting Deals] Failed with status code {response.status_code}")
        print(response.text)
        if response.status_code == 401:
            print("Access token may have expired. Attempting to refresh...")
            return "401"

def refresh_access_token(refresh_token, client_id, client_secret):
    """
    Refresh the Zoho OAuth access token using the refresh token.
    """

    url = "https://accounts.zoho.com/oauth/v2/token"
    
    params = {
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token"
    }
    
    response = requests.post(url, params=params)
    print(response.text)
    if response.status_code == 200:
        print(f"New access token")
        return response.json()["access_token"]
    else:
        print(f"Failed to refresh token: {response.status_code}")
        print(response.text)
        return None
