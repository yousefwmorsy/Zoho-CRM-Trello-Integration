import requests

def set_api_key(apikey, apitoken):
    """
    Set the API key and token for Trello.
    """
    global API_KEY, API_TOKEN

    API_KEY = apikey
    API_TOKEN = apitoken

def create_board(name = ""):
    """
    Create a new Trello board with the given name.
    """

    url = "https://api.trello.com/1/boards/"

    query = {
    'name': f'Project: {name}',
    'key': API_KEY,
    'token': API_TOKEN,
    'defaultLists': 'false'
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )

    print(f"Creating board: {name}")

    if response.status_code == 200:
        print(response.text)
        id = response.json()['id']
        print(f"Created board with ID: {id}")   
        create_list(id, "To Do")
        create_list(id, "In Progress")
        create_list(id, "Done")
        return id
    else:
        print(f"[Creating Board] Failed with status code {response.status_code}")
        print(response.text)
        return None


    
def create_list(id, name):
    """
    Create a new list in the specified Trello board with the given name.
    """

    url = f"https://api.trello.com/1/boards/{id}/lists"
    
    headers = {
    "Accept": "application/json"
    }

    query = {
    'name': f"{name}",
    'key': API_KEY,
    'idBoard': f'{id}',
    'token': API_TOKEN,
    'pos': 'bottom'
    }

    response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
    )

    print(f"Creating list: {name} in board: {id}")

    if response.status_code == 200:
        if(name == "To Do"):
            id_todo = response.json()['id']
            create_card(id_todo, "Kickoff Meeting Scheduled")
            create_card(id_todo, "Requirements Gathering ")
            create_card(id_todo, "System Setup")
    else:
        print(f"[Creating List] Failed with status code {response.status_code}")
        print(response.text)

    
        

def create_card(id, name):
    """
    Create a new card in the specified Trello list with the given name.
    """

    url = "https://api.trello.com/1/cards"

    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': f'{id}',
    'key': API_KEY,
    'token': API_TOKEN,
    'name': f"{name}"
    }

    response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
    )

    print(f"Creating card: {name} in list: {id}")
    if response.status_code != 200:
        print(f"[Creating Card] Failed with status code {response.status_code}")
        print(response.text)
        
    


