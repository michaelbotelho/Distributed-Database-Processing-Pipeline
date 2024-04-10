import socket, subprocess, time
import signal, atexit
import redis, redis.exceptions
import requests, json
from flask_cors import CORS
from flask import Flask, request, jsonify 
from bs4 import BeautifulSoup



app = Flask(__name__)
CORS(app) # Include necessary CORS headers in responses to allow requests from all origins (React Client)
HOST_ADDRESS = 'localhost'
APPLICATION_PORT = None
REDIS_PORT = None
REDIS_PID = None
 

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

''' Not needed (redis server terminated automatically when debug=False in Flask app.run())
@atexit.register
def handle_termination_signal():
    print("Handling Termination")
    # Kill the running redis-server
    subprocess.run(f'taskkill /PID {REDIS_PID} /F', shell=True)
'''



'''Application Routes'''
# Return the status of the Flask API (acts as a ping for client)
@app.route('/status')
def get_status():
    return jsonify({'status': 'running'})


# Receive a query
@app.route('/', methods=['GET', 'POST'])
def receive_query():
    # Simulate client get request
    #with app.test_request_context('/?weeks=2&country=Canada'):
    weeks = request.args.get('weeks')
    country = request.args.get('country')
    sport = request.args.get('sport')
    
    query = request.query_string.decode('utf-8')
    if not query: query=""
                
    # Check if query exists in cache
    if redis_client.exists(query):
        print(f"Exists: {query}")
        response = redis_client.hget(query, 'events')
        return response
    
    
    # Make a request to API service
    scraping_service_url = f'http://{HOST_ADDRESS}:{APPLICATION_PORT}/scrape'
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
                        # Cache query and Return all results back to client if no query parameters given
                        redis_client.hset(query, 'events', json.dumps(response.json()))
                        return jsonify(response.json())
                           
                
            # Cache query and response hset(hash, key, value)
            redis_client.hset(query, 'events', json.dumps(processed_response))

            
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
    with app.app_context():
        # Find open port to run redis server on
        REDIS_PORT = find_open_port(HOST_ADDRESS, start_port=6379)
        # Find open port to run application on
        APPLICATION_PORT = find_open_port(HOST_ADDRESS, start_port=5000, end_port=5004)

        # Startup a redis server if not already running
        redis_running = False
        try:
            redis_client = redis.Redis(host=HOST_ADDRESS, port=REDIS_PORT, decode_responses=True)
        except redis.exceptions.ConnectionError:
            pass
        
        if not redis_running:   
            redis_running = True
            process = subprocess.Popen(f'Redis-x64-3.0.504/redis-server.exe --port {REDIS_PORT}', stdout=subprocess.PIPE)
            REDIS_PID = process.pid # Assign process ID to stop redis server on application termination
        
        
    print(f"Redis: PID({REDIS_PID}) : PORT({REDIS_PORT})")

    print(f"Flask: PORT({APPLICATION_PORT})")
        
        #signal.signal(signal.CTRL_C_EVENT, handle_termination_signal) # Register a signal handler for cleaning up the system when application terminates via CTRL+C
    
    
    # Bind application if port is available 
    if APPLICATION_PORT is None or REDIS_PORT is None: 
        print("Unable to bind service to a port.") 
        exit(0) 
    
    else: 
        app.run(port=APPLICATION_PORT) 