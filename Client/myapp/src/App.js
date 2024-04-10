import React, { useState, useEffect } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import CategoriesMenu from './CategoriesMenu';
import Event from './Event'
import discoverPort from './apiDiscovery';



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
  const [responseData, setResponseData] = useState(null);
  const [sliderValue, setSliderValue] = useState(2);
  const [inputValue1, setInputValue1] = useState('');
  const [inputValue2, setInputValue2] = useState('');


  const handleSliderChange = (event) => {
    setSliderValue(event.target.value);
  };
  const handleInputChange1 = (event) => {
    setInputValue1(event.target.value);
  };
  const handleInputChange2 = (event) => {
    setInputValue2(event.target.value);
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

  // Fetch query when button is clicked
  const fetchData = () => {
    var url = `http://localhost:${flaskPort}/?weeks=${sliderValue}`;
    if (inputValue1 != '') {
      url += `&country=${inputValue1}`;
    }
    if (inputValue2 != '') {
      url += `&sport=${inputValue2}`;
    }
    console.log(url);
    fetch(url)
        .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
        })
        .then(data => {
        console.log('Data received:', data);
        setResponseData(data);
        console.log('Slider value:', sliderValue);
        console.log('Country:', inputValue1);
        console.log('Sport:', inputValue2);
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
            sliderValue={sliderValue}
            onClickSearch={fetchData}
            onSliderChange={handleSliderChange}
            onInputChange1={handleInputChange1}
            onInputChange2={handleInputChange2}
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