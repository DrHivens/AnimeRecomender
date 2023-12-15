import requests

def getAnimeData(name):
    url = f"https://api.jikan.moe/v4/anime?q={name}]"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the Jikan API")
        return None
    
def getAnimeId(data):
    return data['data'][0]['mal_id']

def getAnimeTitle(data):
    return data['data'][0]['title']

def getAnimeRecommendation(id):
    url = f"https://api.jikan.moe/v4/anime/{id}/recommendations"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['data'][:2]
    else:
        print("Failed to fetch data from the Jikan API")
        return None

def getTitles(animeList):
    titles = [anime['entry']['title'] for anime in animeList]
    return titles

animeName = input("Anime name :")
animeId = getAnimeId(getAnimeData(animeName))
print(getTitles(getAnimeRecommendation(animeId)))