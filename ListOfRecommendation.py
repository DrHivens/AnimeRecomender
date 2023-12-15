import json
import requests

def getAnimeData():
    url = "https://api.jikan.moe/v4/recommendations/anime"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()

        extracted_ids = []

        for entry in json_data['data']:
            for anime_entry in entry['entry']:
                mal_id = anime_entry['mal_id']
                extracted_ids.append(mal_id)

        with open("Extracted_MalIds.json", "w") as json_file:
            json.dump(extracted_ids, json_file, indent=4)

        return extracted_ids
    else:
        print("Failed to fetch data from the Jikan API")
        return None


def getAllAnimeRecommendation(id):
    url = f"https://api.jikan.moe/v4/anime/{id}"
    response = requests.get(url)

    if response.status_code == 200:
        anime_data = response.json()['data']
        title = anime_data['title']
        studios = [studio['name'] for studio in anime_data['studios']]
        synopsis = anime_data['synopsis']
        genres = [genre['name'] for genre in anime_data['genres']]

        # dictionary
        anime_info = {
            "title": title,
            "studios": studios,
            "synopsis": synopsis,
            "genres": genres
        }
        return anime_info
    else:
        print("Failed to fetch data from the Jikan API")
        return None


def getStuff():
    with open("Extracted_MalIds.json", "r") as file:
        mal_ids = json.load(file)
    for anime_id in mal_ids:
        anime_info = getAllAnimeRecommendation(anime_id)
        
        if anime_info:
            with open("anime_info.json", "a") as json_file:
                json.dump(anime_info, json_file, indent=4)
                json_file.write("\n")

getStuff()