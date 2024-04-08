import requests 
import socket

from flask import Flask


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


router = Flask(__name__)


@router.route('/')
def send_request():
    data_to_send = {'weeks': '5', 'country' : 'Canada', 'sport' : 'Soccer'}
    response = requests.post('http://127.0.0.1:5000/events', json=data_to_send)
    return response.text


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