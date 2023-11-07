import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.post('/scrap_song')
def scrap_song(body: dict):
    # Retrieve song
    response = requests.get(body['uri'])
    soup = BeautifulSoup(response.content, 'html.parser')
  
    # Store scraped results to variables
    songBody: str = ''
    songTone: str = ''
    songTitle: str = ''
    songWritter: str = ''
    
	# Search for html classes that match song data
    headlines= []
    for headline in soup.find_all('div', class_='cifra-column--left'):
        headlines.append(headline.text)
    print(headlines)
    
	# Returns songs data as json
    return {'body': headlines}

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
    test = soup.find('div', id_='antifonaEntradaMissal')
    print(test)
    
	# Returns liturgy data as json
    return {
        'status': 200,
        'message': 'Liturgy sucessfully scraped from ' + url,
        'scraped_data': {
            'entrance': entrance
        }
    }