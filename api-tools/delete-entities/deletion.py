import requests
import datetime

# Define the API endpoint base
API_URL = "https://onfleet.com/api/v2/"  #Base API URL is here https://onfleet.com/api/v2/
ENTITY = ""   #The Entity you are accessing, see Onfleet API doc for more info

# Define user credentials for Basic Authentication
USERNAME = "" #put your API key here along with ":"
PASSWORD = "" #put nothing here because it's basic auth, see Onfleet API doc for more info

# List of Ids to loop through
id_list = []# array of IDs, task/driver/team/admin

# Loop through each ID and make the API request
for ID in id_list:
    try:
        full_url = f"{API_URL}/{ENTITY}/{ID}"
        response = requests.delete(full_url, auth=(USERNAME, PASSWORD))
        response.raise_for_status()  # Raise an error for bad status codes
        print(f"{ENTITY} {ID} has been deleted\n")
    except requests.exceptions.RequestException as e:
        print(f"API request failed for {ID}: {e}")
    
    start = datetime.datetime.now()
    while (datetime.datetime.now() - start).seconds < 1:
        pass  # Sleep for 1 seconds before the next request, built-in throttle so it would not violate 

# Example cURL command with Basic Auth
# print("\nExample cURL command:")
# print(f"curl -u [REDACTED]:[REDACTED] -X DELETE '{API_URL}?query=YOUR_QUERY'")
