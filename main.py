import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

# This endpoint scraps song data from cifra club
@app.post('/scrap_song_cifra_club')
def scrap_song(body: dict):
    # Retrieve song
    url: str = body['uri']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
  
    # Store scraped results to variables
    songBody: str = ''
    songTone: str = ''
    songTitle: str = ''
    songWritter: str = ''
    
    # Search for html classes that match song data
    body = soup.find('div', class_='cifra-column--left')
    tone = soup.find('span', id='cifra_tom')
    title = soup.find('h1', class_="t1")
    writter = soup.find('h2', class_="t3")

    # Set data to previous created variables
    if body:
        songBody = body.text
    if tone:
        songTone = tone.find('a').text
    if title:
        songTitle = title.text
    if writter:
        songWritter = writter.find('a').text
   
    # Returns songs data as json
    return {
        'status': 200,
        'message': 'Música importada de ' + url,
        'scraped_data': {
            'songBody': songBody,
            'songTone': songTone,
            'songTitle': songTitle,
            'songWritter': songWritter
        }
    }

# This endpoint scraps song data from cifras.com
@app.post('/scrap_song_cifras')
def scrap_song(body: dict):
    # Retrieve song
    url: str = body['uri']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
  
    # Store scraped results to variables
    songBody: str = ''
    songTitle: str = ''
    songWritter: str = ''
    
    # Search for html classes that match song data
    body = soup.find('div', class_='component-song-show-chord-content')
    title = soup.find('span', class_="component-song-show-header__song-title")
    writter = soup.find('a', class_="component-bordered-heading__content")

    # Set data to previous created variables
    if body:
        songBody = body.text
    if title:
        songTitle = title.text
    if writter:
        songWritter = writter.text
   
    # Returns songs data as json
    return {
        'status': 200,
        'message': 'Música importada de ' + url,
        'scraped_data': {
            'songBody': songBody,
            'songTitle': songTitle,
            'songWritter': songWritter
        }
    }

# This endpoint scraps liturgy from pocket terço app
@app.post('/scrap_liturgy')
def scrap_liturgy(body: dict):
    # Retrieve liturgy page
    url: str = 'https://pocketterco.com.br/liturgia/' + body['date']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
	# Store scraped results to variables
    entrance: str = ''
    firstLecture: str = ''
    secondLecture: str = ''
    gospel: str = ''
    psalm: str = ''
    aleluia: str = ''
    offerings: str = ''
    communium: str = ''

    # Search for html classes that match target date content
    entrance = soup.find('div', id_='accorside-1')
    # firstLecture = soup.find('div', id_='accorside-6').text
    
    # Returns liturgy data as json
    return {
        'status': 200,
        'message': 'Liturgy sucessfully scraped from ' + url,
        'scraped_data': {
            'entrance': entrance
        }
    }