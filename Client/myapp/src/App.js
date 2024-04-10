import React, { useState, useEffect } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import CategoriesMenu from './CategoriesMenu';
import Event from './Event'
import discoverPort from './apiDiscovery';
import Slider from './Slider';



function PopulateResults({ data }) {
  const events = [];
  data.forEach(week => {
    week.forEach(sport_event => {
      events.push(
        <Event 
          event_name={sport_event.event_name} 
          sport={sport_event.sport}
          country={sport_event.country}
          locality={sport_event.locality}
          date={sport_event.date}
          />
      );
    });
  });
  return (
    <div id="results">
      {events}
    </div>
  );
}


function App() {
  const [flaskPort, setFlaskPort] = useState(null);
  const [sliderValue, setSliderValue] = useState(2);

  const handleSliderChange = (value) => {
    setSliderValue(value); // Update the slider value
  };

  const handleSubmit = () => {
    console.log('Slider value:', sliderValue);
  };

  // When the component mounts, discover the Flask API port
  useEffect(() => {
    async function discoverFlaskPort() {
      try {
        const port = await discoverPort();
        setFlaskPort(port);
      } catch (error) {
        console.error('Failed to discover Flask API port:', error.message);
      }
    }
    discoverFlaskPort();
  }, []);

  // Once the Flask port is discovered, you can use it to make requests
  useEffect(() => {
    if (flaskPort) {
      // Example: Fetch data from Flask API
      fetch(`http://localhost:${flaskPort}/?weeks=2`)
        .then((response) => response.json())
        .then((data) => {
          console.log('Data from Flask API:', data);
        })
        .catch((error) => {
          console.error('Error fetching data from Flask API:', error.message);
        });
    }
  }, [flaskPort]);


  const data = [[{ 
    "country": "Canada", 
    "date": "4 - 22 April 2024", 
    "event_name": "World Women Chess Championship - Candidates Tournament", 
    "locality": "Toronto", 
    "sport": "Chess" 
  }]];
  return (
    <main>
      <div id="categories-menu">
        <CategoriesMenu
          sliderValue={sliderValue}
          onSliderChange={handleSliderChange}
          onSubmit={handleSubmit}
        />
      </div>
      <div id="results-container">
        <h3>Results</h3>
        <PopulateResults data={[[{ 
          "country": "Canada", 
          "date": "4 - 22 April 2024", 
          "event_name": "World Women Chess Championship - Candidates Tournament", 
          "locality": "Toronto", 
          "sport": "Chess" 
        }], 
        [{ 
          "country": "Canada", 
          "date": "4 - 22 April 2024", 
          "event_name": "World Women Chess Championship - Candidates Tournament", 
          "locality": "Toronto", 
          "sport": "Ohio" 
        }]]} />
      </div>
    </main>
  );
}


export default App;