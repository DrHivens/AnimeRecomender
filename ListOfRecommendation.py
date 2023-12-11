import json
import requests

# get anime ids of all 100 anime
# make serperate search for these 100 anime 
# then crossref with the anime

def getAnimeData():
    url = "https://api.jikan.moe/v4/recommendations/anime"

    # Making a GET request to the Jikan API
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        extracted_ids = []

        for entry in json_data['data']:
            for anime_entry in entry['entry']:
                mal_id = anime_entry['mal_id']
                extracted_ids.append(mal_id)

        # Writing extracted IDs to a JSON file
        with open("Extracted_MalIds.json", "w") as json_file:
            json.dump(extracted_ids, json_file, indent=4)  # Indent for pretty formatting

        return extracted_ids
    else:
        print("Failed to fetch data from the Jikan API")
        return None

# Call the function to get and process data
#getAnimeData()


def getAllAnimeRecommendation(id):
    url = f"https://api.jikan.moe/v4/anime/{id}"
    
    # Making a GET request to the Jikan API for the specific anime ID
    response = requests.get(url)

    if response.status_code == 200:
        anime_data = response.json()['data']

        # Extracting specific information
        title = anime_data['title']
        studios = [studio['name'] for studio in anime_data['studios']]
        synopsis = anime_data['synopsis']
        genres = [genre['name'] for genre in anime_data['genres']]

        # Constructing the extracted information into a dictionary
        anime_info = {
            "title": title,
            "studios": studios,
            "synopsis": synopsis,
            "genres": genres
            # Add more information extraction as needed
        }

        # Writing extracted data to a JSON file
        #with open(f"Anime_Info.json", "w") as json_file:
            #json.dump(anime_info, json_file, indent=4)  # Indent for pretty formatting

        return anime_info
    else:
        print("Failed to fetch data from the Jikan API")
        return None


def getStuff():
    # Read the list of IDs from Extracted_MalIds.json
    with open("Extracted_MalIds.json", "r") as file:
        mal_ids = json.load(file)

    # Iterate through each ID and fetch anime information
    for anime_id in mal_ids:
        anime_info = getAllAnimeRecommendation(anime_id)
        
        if anime_info:
            # Append the result of the function to anime_info.json
            with open("anime_info.json", "a") as json_file:
                json.dump(anime_info, json_file, indent=4)  # Indent for pretty formatting
                json_file.write("\n")  # Add a new line for separating entries


# Call getStuff function
getStuff()