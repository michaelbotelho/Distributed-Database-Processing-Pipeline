from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def scrape_events():
    # URL of the website to scrape
    url = 'https://allsportdb.com/?week={0}'
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Extract and Parse the HTML content of the page
    events = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Iterate through each row in table (event represented by a row)
        event_items = soup.find_all('tr')
        for event_item in event_items:
            # Ensure table row is an event (otherwise operations will return none types)
            if (event_item.get('itemtype') == 'http://schema.org/Event'):                
                event_name = event_item.find('a', class_='text-primary')
                sport = event_item.find('a', {'href': lambda x : x.startswith('/Sports/')})
                country = event_item.find('meta', itemprop='addressCountry')
                locality = event_item.find('meta', itemprop='addressLocality')
                datetime = event_item.find_all('td')[-1]
                events.append({
                    'event_name': event_name.get_text(),
                    'country': country.get('content'),
                    'locality': locality.get('content'),
                    'datatime': datetime.get_text().strip(),
                    'sport': sport.get_text()
                })
    
    # Render a template with the extracted data
    return jsonify(events)


if __name__ == "__main__":
    app.run(debug=True)