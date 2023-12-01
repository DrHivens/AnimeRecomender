import requests
import json

#Draw the algorithm
#Create the algoithm
#https://www.datacamp.com/tutorial/making-http-requests-in-python
#https://jikan.docs.apiary.io/#introduction/jikan
#https://docs.api.jikan.moe/#tag/anime/operation/getAnimeFullById
#https://github.com/jikan-me/jikan-rest/issues/189
#https://docs.api.jikan.moe/


def getAnimeData():
    url = "https://api.jikan.moe/v4/anime?q=Dr stone"

    # Making a GET request to the Jikan API
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        # if i want to write a json file 
        #with open("AnimeData.json", "w") as json_file:
            #json.dump(json_data, json_file, indent=4)  # Indent for pretty formatting

        return json_data
    else:
        print("Failed to fetch data from the Jikan API")
        return None
    
#all info on that anime    
anime_data = getAnimeData()

def getAnimeTitle(data):
    return data['data'][0]['title']

def getAnimeStudio(data):
    return data['data'][0]['studios'][0]['name']

def getAnimeGenre(data):
    return [genre['name'] for genre in data['data'][0]['genres']]

def getAnimeDescription(data):
    return data['data'][0]['synopsis']

print(getAnimeTitle(anime_data))
print(getAnimeStudio(anime_data))
print(getAnimeGenre(anime_data))
print(getAnimeDescription(anime_data))

#create the user input
#Saturday:
#get the list of anime
#get data on those anime and stock them in lists
#Pause and rethink path
#get list of recommendation and pre parse them

#Sunday:
#run a function on the reommendation to get their score
