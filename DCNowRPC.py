import requests
import json
from pypresence import Presence
import time

# Set the player username(s) you want to track
primaryUsername = "Your-Dreacast-Now!-username"
secondaryUsername = "" # Leave blank if not needed

print("Starting DCNowRPC!")

# Function to fetch player data
def fetch_player_data(primaryUsername, secondaryUsername):
    try:
        response = requests.get("http://dreamcast.online/now/api/users.json")
        response.raise_for_status()  # Check if the request was successful
        data = json.loads(response.text)

        # Check for primary username
        for player in data['users']:
            if player['username'] == primaryUsername:
                print(f"Found {player['username']} playing {player['current_game_display']}")
                return player['current_game_display'], player['level']

        print(f"Unable to find an online player with the username {primaryUsername}.")

        if secondaryUsername:
            # If primary username is not found, check for secondary username
            for player in data['users']:
                if player['username'] == secondaryUsername:
                    print(f"Found {player['username']} playing {player['current_game_display']}")
                    return player['current_game_display'], player['level']

            print(f"Unable to find an online player with the username {secondaryUsername}.")

        # Return 'Not found' if neither primary nor secondary usernames are in the list
        return "Not found", "Not found"

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error", "Error"


# Initialize Discord Rich Presence
client_id = "1148170188483743744"
RPC = Presence(client_id)

# Try to connect to Discord Client
try:
    RPC.connect()
except Exception as e:
    print(f"Could not connect to Discord: {e}")
    exit(1)

# Main loop to update Discord Rich Presence
while True:
    game_name, level = fetch_player_data(primaryUsername, secondaryUsername)

    # Replace spaces with '-', remove colons, periods, exclamation marks, and convert to lowercase
    asset_key = game_name.replace(" ", "-").replace(":", "").replace(".", "").replace("!", "").lower()

    # If game name is empty, set game_name to "Unknown" and asset_key to "unknown"
    if not game_name:
        game_name = "Unknown"
        asset_key = "unknown"

    # Update Discord Rich Presence
    # If the player is not in a game, display "Console Disconnected"
    if game_name == "Not found":
        RPC.update(details=f"Console Disconnected", state=f"Player Offline")
    else:
        # Check if asset_key is empty
        if asset_key:
            RPC.update(details=f"Playing {game_name}", state=f"{level}", large_image=asset_key)
        else:
            # Update without large_image if asset_key is empty
            RPC.update(details=f"Playing {game_name}", state=f"{level}")

    # Wait for 15 seconds before updating again
    time.sleep(15)
