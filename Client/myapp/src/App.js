import React, { useState, useEffect } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import CategoriesMenu from './CategoriesMenu';
import Event from './Event'
import discoverPort from './apiDiscovery';
import Slider from './Slider';



function PopulateResults({ data }) {
  const events = [];
  data && console.log(data[0]);
  data && data.forEach(week => {
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


  // useEffect(() => {
  //   if (flaskPort) {
  //     // Example: Fetch data from Flask API
  //     fetch(`http://localhost:${flaskPort}/?weeks=2`)
  //       .then((response) => response.json())
  //       .then((data) => {
  //         console.log('Data from Flask API:', data);
  //       })
  //       .catch((error) => {
  //         console.error('Error fetching data from Flask API:', error.message);
  //       });
  //   }
  // }, [flaskPort]);

  const [responseData, setResponseData] = useState(null);
  const fetchData = () => {
    fetch(`http://localhost:${flaskPort}/?weeks=3`)
        .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
        })
        .then(data => {
        console.log('Data received:', data);
        setResponseData(data);
        })
        .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    }); 
  };

  if (flaskPort) {
    return (
      <main>
        <div id="categories-menu">
          <CategoriesMenu
            onClick={fetchData}
            sliderValue={sliderValue}
            onSliderChange={handleSliderChange}
            onSubmit={handleSubmit}
          />
        </div>
        <div id="results-container">
          <h3>Results</h3>
          <PopulateResults data={responseData} />
        </div>
      </main>
    );
  }
  else {
    return (
      <h3>No Server Found</h3>
    );
  }
}


export default App;