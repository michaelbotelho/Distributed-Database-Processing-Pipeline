import React, { useState, useEffect } from 'react';
import './App.css'; 
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import CategoriesMenu from './CategoriesMenu'; 
import Event from './Event'
import discoverPort from './apiDiscovery';



function PopulateResults({ data }) {
  const events = [];
  data.forEach(week => {
    week.forEach(sport_event => {
      events.push(
        <Event event={sport_event} />
      );
    });
  });
  return (
    <div id="results">
      {events}
    </div>
  );
}


async function App() {
  try {
    const response = await fetch(`localhost:8000/proxy`);
    if (response.ok) {
      // Proxy is up, handle program logic
    }
  } catch (error) {
    console.error("Error no proxy at localhost:8000/proxy");
  }
  
  // const [flaskPort, setFlaskPort] = useState(null);

  // // When the component mounts, discover the Flask API port
  // useEffect(() => {
  //   async function discoverFlaskPort() {
  //     try {
  //       const port = await discoverPort();
  //       setFlaskPort(port);
  //     } catch (error) {
  //       console.error('Failed to discover Flask API port:', error.message);
  //     }
  //   }
  //   discoverFlaskPort();
  // }, []);
  // console.log("STEP 1")

  // // Once the Flask port is discovered, you can use it to make requests
  // useEffect(() => {
  //   if (flaskPort) {
  //     // Example: Fetch data from Flask API
  //     fetch(`http://localhost:${flaskPort}/?weeks=1`)
  //       .then((response) => response.json())
  //       .then((data) => {
  //         console.log('Data from Flask API:', data);
  //         return (
  //           <main>
  //             <p id="site-description">Presents information about all upcoming sports events that match your filters. Or search without any filters to see this weeks sport events.</p>
  //             <div id="categories-menu">
  //               <CategoriesMenu />
  //             </div>
  //             <div id="results-container">
  //               <h3>Results</h3>
  //               <PopulateResults data={data} />
  //             </div>
  //           </main>
  //         );
  //       })
  //       .catch((error) => {
  //         console.error('Error fetching data from Flask API:', error.message);
  //       });
  //   }
  // }, [flaskPort]);


  return (
    <main>
      <p id="site-description">Presents information about all upcoming sports events that match your filters. Or search without any filters to see this weeks sport events.</p>
      <div id="categories-menu">
        <CategoriesMenu />
      </div>
      <div id="results-container">
        <h3>Results</h3>
        {/* <PopulateResults /> */}
      </div>
    </main>
  );
}


export default App;