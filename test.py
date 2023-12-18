import requests

def getAnimeData(name):
    url = f"https://api.jikan.moe/v4/anime?q={name}]"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the Jikan API with name.")
        return None
    
def getAnimeId(data):
    return data['data'][0]['mal_id']

def getAnimeImage(data):
    return data['data'][0]['image_url']


def getAnimeRecommendation(id):
    url = f"https://api.jikan.moe/v4/anime/{id}/recommendations"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['data'][:2]
    else:
        print("Failed to fetch data from the Jikan API with Id")
        return None

def getTitles(animeList):
    titles = [anime['entry']['title'] for anime in animeList]
    return titles

def getImagesUrl(animeList):
    urls = [anime['entry']['images']['jpg']['image_url'] for anime in animeList]
    return urls

animeName = input("Anime name :")
animeId = getAnimeId(getAnimeData(animeName))
print(getTitles(getAnimeRecommendation(animeId)))
print(getImagesUrl(getAnimeRecommendation(animeId)))