const PORT_RANGE = [5000, 5004]; // Flask API port range to scan

async function discoverPort() {
  for (let port = PORT_RANGE[0]; port <= PORT_RANGE[1]; port++) {
    try {
      const response = await fetch(`http://localhost:${port}/status`);
      if (response.ok) {
        // Flask API is running on this port
        return port;
      }
    } catch (error) {
      // Handle errors or continue to the next port
      console.error(`Error checking port ${port}: ${error.message}`);
    }
  }
  // If no valid port is found
  throw new Error('Flask API not found on any port in the range');
}

export default discoverPort;