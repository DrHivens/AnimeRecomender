import requests
from collections import Counter
import spacy


#Draw the algorithm
#Create the algoithm
#https://www.datacamp.com/tutorial/making-http-requests-in-python
#https://jikan.docs.apiary.io/#introduction/jikan
#https://docs.api.jikan.moe/#tag/anime/operation/getAnimeFullById
#https://github.com/jikan-me/jikan-rest/issues/189
#https://docs.api.jikan.moe/


def getAnimeData(name):
    url = f"https://api.jikan.moe/v4/anime?q={name}]"

    # Making a GET request to the Jikan API
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        #checks if data is empty in json file
        if 'data' in json_data and len(json_data['data']) == 0:
            print(f"No anime found with the name '{name}'")
            return None

        # if i want to write a json file 
        #with open("AnimeData.json", "w") as json_file:
            #json.dump(json_data, json_file, indent=4)  # Indent for pretty formatting

        return json_data
    else:
        print("Failed to fetch data from the Jikan API")
        return None
    
#all info on that anime    
#anime_data = getAnimeData()

def getAnimeTitle(data):
    return data['data'][0]['title']

def getAnimeStudio(data):
    return data['data'][0]['studios'][0]['name']

def getAnimeGenre(data):
    return [genre['name'] for genre in data['data'][0]['genres']]

def getAnimeDescription(data):
    return data['data'][0]['synopsis']



#create the user input
#Saturday:
#get the list of anime
#get data on those anime and stock them in lists
#Pause and rethink path
#get list of recommendation and pre parse them

#Sunday:
#run a function on the reommendation to get their score




animeList = input("Write down your favorite anime seperated with a coma ,  :")
animeList = animeList.split(',')
#print(animeList)

animeListGenreRaw = []
animeListGenre = []
animeListStudio = []
animeListDescription = []

for i in animeList:
    anime = getAnimeData(i)
    animeListGenreRaw.extend(getAnimeGenre(anime)) # do i want to remove duplicates or nah
    animeListStudio.append(getAnimeStudio(anime))
    animeListDescription.append(getAnimeDescription(anime))
    #print(getAnimeGenre(anime))

genre_counts = Counter(animeListGenreRaw)
#print(animeListDescription)
# Filter only the genres that appear more than once
for genre, count in genre_counts.items():
    if count > 1:
        animeListGenre.append(genre)

#print(animeListGenre)

#print(animeListStudio)

#def getAnimeListProperties():


nlp = spacy.load("en_core_web_sm")


# its meh not the best... will have to think it through ---> needs better filtering
for description in animeListDescription:
    doc = nlp(description)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct and token.pos_ != 'DET']
    keywordsSummary = list(set(keywords))
    print(keywordsSummary)