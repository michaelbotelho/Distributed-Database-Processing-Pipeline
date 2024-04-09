import socket 
import requests
from flask import Flask, jsonify 


router = Flask(__name__)


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

def check_status_of_endpoint(address, port): 
    try: 
        with socket.create_connection((address, port), timeout=1) as connection: 
            print("API Endpoint Found") 
            return True 
    except OSError: 
        return False 
    

# Relay query to API service 
@router.route('/query') 
def receive_query(): 
    weeks = 3 
    country = "Canada" 
    sport = "Soccer" 
    
    # Search for active server on port range (defined in API service) 
    for port in range(5000, 5002 + 1): 
        api_url = f'http://localhost:{port}/' 
        if check_status_of_endpoint('localhost', port): 
            # Make a request to API service 
            response = requests.get(api_url, params={'weeks': weeks, 'country': country, 'sport': sport}) 
            return response.json() 
        return jsonify(None) 


if __name__ == '__main__': 
    # Specify port range to scan
    # Router services will run from ports 5003 to 5005 when on the same machine (max 3 services on one machine) 
    start_port = 5003 
    end_port = 5005 
    address = "localhost" 
    
    # Scan for open port to bind application to 
    port = find_open_port(address, start_port, end_port) 
    
    # Bind application if port is available 
    if port is None: 
        print("No open ports found in the specified range.") 
        exit(0) 
    else: 
        router.run(debug=True, port=port)