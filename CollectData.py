import requests
import json
from flask import Flask, Response, jsonify
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


app = Flask(__name__)


def scrape_sports_events(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Extract and Parse the HTML content of the page if request successful
    events_list = []
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
                date = event_item.find_all('td')[-1]
                
                # Create JSON objects with scraped data and set default values in case attribute cant be found
                events_list.append({
                    'event_name': event_name.get_text() if event_name else None,
                    'country': country.get('content') if country else None,
                    'locality': locality.get('content') if locality else None,
                    'date': date.get_text().strip() if date else None,
                    'sport': sport.get_text() if sport else None
                })
    yield json.dumps(events_list).encode('utf-8')


# GET /Events
@app.route("/Events/", defaults={'weeks': 0})
@app.route("/Events/<int:weeks>")
def process_request(weeks):    
    # Submit each call to a thread pool to speed up execution time
    with ThreadPoolExecutor() as executor:
        if weeks == 0: # Base case for unspecified amount of weeks (default to 1 week, the current one)
            url = f'https://allsportdb.com/?week={weeks}'
            futures = [executor.submit(scrape_sports_events, url)]
        else:
            urls = [f'https://allsportdb.com/?week={week}' for week in range(weeks)]
            futures = [executor.submit(scrape_sports_events, url) for url in urls]
            
        # Yield results from each thread as they are available
            # yields collection of lists, each list represents one page and contains JSON objects of event data
        for future in futures:
            yield from future.result()


def generate_events(url):
    for events in scrape_sports_events(url):
        yield json.dumps(events).encode('utf-8')


if __name__ == "__main__":
    app.run(debug=True)