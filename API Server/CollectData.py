import requests
import socket

from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


api = Flask(__name__)


def find_open_port(address, start_port, end_port):
    """
    Scans a range of ports for an available port to bind the given address to.
    
    Parameters:
        address (string): The desired url of the service.
        start_port (int): The smallest port to bind the service to.
        end_port (int): The largest port to bind the service to.
    """
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((address, port))
                return port
            except OSError:
                pass
    return None


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
        return events_list
        # yield json.dumps(events_list).encode('utf-8')
    else:
        return None
        # yield json.dumps(None).encode('utf-8')
        
        
''' Routing functions ''' 
''' GET /Events
@api.route("/events", methods=['POST'])
def process_request():
    # Simulate a url query
    #with app.app_context():    
    with app.test_request_context('/?weeks=2'):
        # Parse weeks argument (context issue when not enclosed in this with statement)
        if request.args:
            weeks = request.args.get('weeks')  
            if not weeks:
                weeks = 0
            else:
                weeks = int(weeks)
        else:
            weeks = 0

            
    # Submit each call to a thread pool to speed up execution time
    with ThreadPoolExecutor() as executor:
        if weeks == 0: # Base case for unspecified amount of weeks (default to 1 week, the current one)
            url = f'https://allsportdb.com/?week={0}'
            futures = [executor.submit(scrape_sports_events, url)]
        else:
            urls = [f'https://allsportdb.com/?week={week}' for week in range(weeks)]
            futures = [executor.submit(scrape_sports_events, url) for url in urls]
            
        # Yield results from each thread as they are available
            # yields collection of lists, each list represents one page and contains JSON objects of event data
        for future in futures:
            if (future.result() == None):
                print("error")
            yield from future.result()

    return f"Get {weeks} weeks"
'''


@api.route("/", methods=['GET'])
def receive_query():
    if request.method == 'GET':
        weeks = request.args.get('weeks')
        country = request.args.get('country')
        sport = request.args.get('sport')
        
        response = [] # {'weeks' : weeks, 'country' : country, 'sport' : sport}
        if not weeks or int(weeks) == 0:
            response_data = scrape_sports_events(url=f'https://allsportdb.com/?week={0}')
            if response_data:
                response.append(response_data)
        else :
            for week in range(int(weeks)):
                response_data = scrape_sports_events(url=f'https://allsportdb.com/?week={week}')
                if response_data:
                    response.append(response_data)
            
        return jsonify(response)

    

if __name__ == "__main__":
    # Specify port range to scan 
    # API services will run from ports 5000 to 5004 when on the same machine (max 3 services on one machine)
    start_port = 5000
    end_port = 5002
    address = "localhost"
    
    # Scan for open port to bind application to
    port = find_open_port(address, start_port, end_port)
    
    # Bind application if port is available
    if port is None:
        print("No open ports found in the specified range.")
        exit(0)
    else:
        api.run(debug=True, port=port)
    