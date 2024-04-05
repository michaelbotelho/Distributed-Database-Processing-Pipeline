import React from 'react';
import './App.css'; 
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import CategoriesMenu from './CategoriesMenu'; 
import Events from './Event'



function PopulateResults({ events }) {
  return <Event />
}

function App() {
  return (
    <main>
      <div id="categories-menu">
        <CategoriesMenu />
      </div>
      <div id="results-container">
        <h3>Results</h3>
        <PopulateResults />
      </div>
    </main>
  );
}

export default App;