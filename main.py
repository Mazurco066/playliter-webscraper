import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)

# This endpoint scraps song data from cifra club
@app.route('/scrap_song_cifra_club', methods=['POST'])
def scrap_song_cifra_club():
    # Retrieve song
    url = request.json['uri']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
  
    # Store scraped results to variables
    songBody = ''
    songTone = ''
    songTitle = ''
    songWritter = ''
    
    # Search for html classes that match song data
    body = soup.find('div', class_='cifra-column--left')
    tone = soup.find('span', id='cifra_tom')
    title = soup.find('h1', class_="t1")
    writter = soup.find('h2', class_="t3")

    # Set data to previously created variables
    if body:
        songBody = body.text
    if tone:
        songTone = tone.find('a').text
    if title:
        songTitle = title.text
    if writter:
        songWritter = writter.find('a').text
   
    # Returns songs data as json
    return jsonify({
        'status': 200,
        'message': f'Música importada de {url}',
        'scraped_data': {
            'songBody': songBody,
            'songTone': songTone,
            'songTitle': songTitle,
            'songWritter': songWritter
        }
    })

# This endpoint scraps song data from cifras.com
@app.route('/scrap_song_cifras', methods=['POST'])
def scrap_song_cifras():
    # Retrieve song
    url = request.json['uri']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
  
    # Store scraped results to variables
    songBody = ''
    songTitle = ''
    songWritter = ''
    
    # Search for html classes that match song data
    body = soup.find('div', class_='component-song-show-chord-content')
    title = soup.find('span', class_="component-song-show-header__song-title")
    writter = soup.find('a', class_="component-bordered-heading__content")

    # Set data to previously created variables
    if body:
        songBody = body.text
    if title:
        songTitle = title.text
    if writter:
        songWritter = writter.text
   
    # Returns songs data as json
    return jsonify({
        'status': 200,
        'message': f'Música importada de {url}',
        'scraped_data': {
            'songBody': songBody,
            'songTitle': songTitle,
            'songWritter': songWritter
        }
    })

if __name__ == '__main__':
    app.run(debug=False)