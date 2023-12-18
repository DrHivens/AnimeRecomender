import json
import requests
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

def getAnimeStudio(data):
    return data['data'][0]['studios'][0]['name']

def getAnimeGenre(data):
    return [genre['name'] for genre in data['data'][0]['genres']]

def getAnimeDescription(data):
    return data['data'][0]['synopsis']


def handler(listOfAnimeName):
    animeListGenreRaw = []
    animeListGenre = []
    animeListStudio = []
    animeListDescriptionRaw = []
    animeListDescription = []

    filtiredNames = [i for i in listOfAnimeName if getAnimeData(i) is not None]

    for i in filtiredNames:
        anime = getAnimeData(i)
        if anime is not None:
            animeListGenreRaw.extend(getAnimeGenre(anime))
            animeListStudio.append(getAnimeStudio(anime))
            animeListDescriptionRaw.append(getAnimeDescription(anime))

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
        "studios": animeListStudio,
        "synopsis": animeListDescription,
        "genres": animeListGenre,
    }

    with open("MyAnimeList.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)



#stackoverflow code and copilot
def load_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)
    

def getRec(info, list):
    mySynopsis = ' '.join(info['synopsis'])
    myGenres = ' '.join(info['genres'])

    vectorizer = CountVectorizer().fit([mySynopsis, myGenres])

    topAnimes = []  # Store top similar items
    similarities = []  # Store corresponding similarity scores

    for item in list:
        itemSynopsis = item.get('synopsis', '')
        itemGenres = ' '.join(item.get('genres', []))

        vector = vectorizer.transform([itemSynopsis, itemGenres])
        similarity = cosine_similarity(vector)[0][0]  # Extract the similarity value

        if len(topAnimes) < 5:
            topAnimes.append(item.get('title', ''))
            similarities.append(similarity)
        else:
            min_similarity_index = similarities.index(min(similarities))
            if similarity > similarities[min_similarity_index]:
                topAnimes[min_similarity_index] = item.get('title', '')
                similarities[min_similarity_index] = similarity

    return topAnimes
#end of help



animeList = input("Write down your favorite anime seperated with a coma ,  :")
animeList = animeList.split(',')

handler(animeList)
myAnimeTaste = load_data('MyAnimeList.json')
trendingAnimeList = load_data('Anime_info.json')

recommmendedAnime = getRec(myAnimeTaste, trendingAnimeList)
print(recommmendedAnime)