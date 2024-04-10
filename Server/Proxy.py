import requests
from flask import Flask, request, jsonify



app = Flask(__name__)

# Define the URLs of the Raft nodes (Flask applications)
RAFT_NODES = [
    'http://localhost:5000',  # Raft node 1 URL
    'http://localhost:5001',  # Raft node 2 URL
    'http://localhost:5002',  # Raft node 3 URL
    'http://localhost:5003',  # Raft node 4 URL
    'http://localhost:5004'   # Raft node 5 URL
]

@app.route('/proxy', methods=['GET'])
def forward_request_to_raft():
    # Example request: (this will be given by the client)
    with app.test_request_context('/?weeks=2&country=Canada'):
        query = request.query_string.decode('utf-8')
        if not query: query=""
    
    # Forward the request to one of the Raft nodes
    for raft_node in RAFT_NODES:
        try:
            # Check if node at current address exists (response will be url of leader node)
            response = requests.get(raft_node + '/status')
            if response.status_code == 200:
                # Forward query to leader node 
                response = requests.get(response.json(), params=query)
                return jsonify(response.json()), 200
            
        except requests.RequestException as e:
            # Handle connection errors 
            print(f"Error connecting to Raft node {raft_node}: {e}")
            continue

    # If no Raft node responds successfully, return an error response
    return jsonify({'error': 'Failed to connect to Raft cluster'}), 500

if __name__ == '__main__':
    # Run the entry point Flask application
    app.run(host='localhost', port=8000)