import os, socket, subprocess, time, re
import redis
import requests
import json
from flask import Flask, request, jsonify 
from bs4 import BeautifulSoup


app = Flask(__name__)
HOST_ADDRESS = 'localhost'


def find_open_port(address, start_port, end_port=65534):
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
                break
            except OSError:
                pass
    return None

def check_status_of_endpoint(address, port): 
    try: 
        with socket.create_connection((address, port), timeout=1) as connection: 
            print("API Endpoint Found") 
            return True 
    except OSError: 
        return False 
 
    # Start the Redis server as a subprocess
    subprocess.Popen('redis-cli shutdown', shell=True)
    # Give some time for the server to start up
    time.sleep(1)   
    
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
    else:
        return None

def delete_all_keys():
    keys = redis_client.keys("*")
    print(f'Keys Before: {keys}')
    for i in range(len(keys)):
        redis_client.delete(keys[i])
    print(f'Keys Left: {redis_client.keys("*")}')


'''Application Routes'''
# Receive a query
@app.route('/', methods=['GET'])
def receive_query():
    # Simulate client get request
    with app.test_request_context('/?weeks=2&country=United States'):
        weeks = request.args.get('weeks')
        country = request.args.get('country')
        sport = request.args.get('sport')
        
        query = request.query_string
                
    # Check if query exists in cache
    if redis_client.exists(query.decode('utf-8')):
        print(f"Exists: {query.decode('utf-8')}")
        response = redis_client.hget(query.decode('utf-8'), 'events')
        return jsonify(response)
    
    
    # Make a request to API service
    scraping_service_url = f'http://{HOST_ADDRESS}:{APPLICATION_PORT-1}/scrape'
    response = requests.get(scraping_service_url, params={'weeks': weeks})


    # Check if the response is successful
    if response.status_code == 200:
        try:
            # Process data to match query
            processed_response = []
            for events_week in response.json():
                for event in events_week:
                    if country:
                        if sport and event['country'] == country and event['sport'] == sport:
                            # Add event if country and sport are given and both match
                            processed_response.append(event)
                        elif not sport and event['country'] == country:
                            # Add event if sport doesn't exist but country does and matches
                            processed_response.append(event)
                    elif sport and event['sport'] == sport:
                        # Add event if country doesn't exist but sport does and matches
                        processed_response.append(event)
                    else:
                        # Return all results back to client if no query parameters given
                        return jsonify(response.json())
                           
                
            # Cache query and response hset(hash, key, value)
            redis_client.hset(query.decode('utf-8'), 'events', json.dumps(processed_response))

            
            # Send response back to client
            return jsonify(processed_response)
        
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return jsonify({'error': 'Invalid JSON format in response'})
    else:
        print(f"Error: {response.status_code}")
        return jsonify({'error': 'Failed to fetch data from API service'})


# Collect data in range of weeks (default weeks=0)
@app.route("/scrape", methods=['GET'])
def collect_data():
    if request.method == 'GET':
        weeks = request.args.get('weeks')

        response = [] 
        if not weeks or int(weeks) == 0:
            response_data = scrape_sports_events(url=f'https://allsportdb.com/?week={0}')
            if response_data:
                response.append(response_data)
        else:
            for week in range(int(weeks)):
                response_data = scrape_sports_events(url=f'https://allsportdb.com/?week={week}')
                if response_data:
                    response.append(response_data)

        return jsonify(response)
    

if __name__ == '__main__': 
    # Scan for open port to bind application to 
    APPLICATION_PORT = find_open_port(HOST_ADDRESS, start_port=5000, end_port=5004)
    # Run Redis server and find port number
    REDIS_PORT = None
    redis_server_path = "Redis-x64-3.0.504"
    process = subprocess.Popen(f'"../{redis_server_path}/redis-server.exe"', stdout=subprocess.PIPE)
    # Read the output of the Redis server process
    while True:
        output = process.stdout.readline().decode('utf-8')
        re1 = re.search(r"\*:\d{4}", output)
        re2 = re.search(r"port \d{4}", output)
        if re1:
            REDIS_PORT = re1.group(0).split(":")[1]
            break
        if re2:
            REDIS_PORT = re2.group(0).split()[1]
            break
        if not output:
            break
        
    # Bind application if port is available 
    if APPLICATION_PORT is None or REDIS_PORT is None: 
        print("No open ports found in the specified range.") 
        exit(0) 
    else: 
        redis_client = redis.Redis(host=HOST_ADDRESS, port=REDIS_PORT, decode_responses=True)
        app.run(debug=True, port=APPLICATION_PORT) # Weird bug where application binds to PORT and print returns PORT + 1