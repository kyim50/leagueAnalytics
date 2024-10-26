import requests
from riotwatcher import LolWatcher, ApiError
from config import API_KEY

watcher = LolWatcher(API_KEY)

def get_summoner_puuid_by_riot_id(game_name, tag_line, region='americas'):
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {"X-Riot-Token": API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()['puuid']
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print("Riot ID not found.")
        elif response.status_code == 401:
            print("Unauthorized - check your API key.")
        else:
            print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
    return None

def get_match_history(region, puuid, count=10):
    try:
        match_history = watcher.match.matchlist_by_puuid(region, puuid, count=count)
        return match_history
    except ApiError as err:
        print(f"Failed to retrieve match history: {err}")
        return None

def retrieve_match_data(game_name, tag_line):
    print(f"Requesting summoner data for '{game_name}#{tag_line}'")
    puuid = get_summoner_puuid_by_riot_id(game_name, tag_line)
    
    if not puuid:
        print("Failed to retrieve PUUID for summoner.")
        return None
    
    match_history = get_match_history("americas", puuid)
    return match_history

