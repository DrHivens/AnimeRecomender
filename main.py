import json
import requests
from collections import Counter
import spacy

#https://www.datacamp.com/tutorial/making-http-requests-in-python
#https://jikan.docs.apiary.io/#introduction/jikan
#https://docs.api.jikan.moe/#tag/anime/operation/getAnimeFullById
#https://github.com/jikan-me/jikan-rest/issues/189
#https://docs.api.jikan.moe/
#https://docs.python.org/3/library/collections.html#collections.Counter


def getAnimeData(name):
    url = f"https://api.jikan.moe/v4/anime?q={name}]"

    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        if 'data' in json_data and len(json_data['data']) == 0:
            print(f"No anime found with the name '{name}'")
            return None
        
        return json_data
    else:
        print("Failed to fetch data from the Jikan API")
        return None
    

def getAnimeTitle(data):
    return data['data'][0]['title']

def getAnimeStudio(data):
    return data['data'][0]['studios'][0]['name']

def getAnimeGenre(data):
    return [genre['name'] for genre in data['data'][0]['genres']]

def getAnimeDescription(data):
    return data['data'][0]['synopsis']


animeList = input("Write down your favorite anime seperated with a coma ,  :")
animeList = animeList.split(',')


def handler(listOfAnimeName):
    animeListGenreRaw = []
    animeListGenre = []
    animeListStudio = []
    animeListDescriptionRaw = []
    animeListDescription = []

    filtered_anime_names = [i for i in listOfAnimeName if getAnimeData(i) is not None]

    for i in filtered_anime_names:
        anime = getAnimeData(i)
        if anime is not None:
            animeListGenreRaw.extend(getAnimeGenre(anime))
            animeListStudio.append(getAnimeStudio(anime))
            animeListDescriptionRaw.append(getAnimeDescription(anime))

    #genre_counts = Counter(animeListGenreRaw)
    # Filter only the genres that appear more than once
    #for genre, count in genre_counts.items():
        #if count > 1:
            #animeListGenre.append(genre)

    nlp = spacy.load("en_core_web_sm")

    for description in animeListDescriptionRaw:
        doc = nlp(description)
        keywords = [token.text for token in doc if not token.is_stop and not token.is_punct and token.pos_ != 'DET']
        animeListDescription.extend(keywords)

    # Convert lists to sets to remove duplicates
    animeListGenre = list(set(animeListGenreRaw))
    animeListDescription = list(set(animeListDescription))

    # Write attributes to a JSON file
    data = {
        "Studio": animeListStudio,
        "Description": animeListDescription,
        "Genre": animeListGenre,
        "Filtered_Anime_Names": filtered_anime_names
    }

    with open("MyAnimeList.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)




handler(animeList)