import React from 'react';
import './App.css'; // Your custom CSS file
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import CategoriesMenu from './CategoriesMenu'; // Import your CategoriesMenu component

function App() {
  return (
    <main>
      <div id="categories-menu">
        <CategoriesMenu />
      </div>
      <div id="results-container">
        <p>Results</p>
        <p>Another</p>
        <p>Grid Element</p>
        <p>Anothersld</p>
      </div>
    </main>
  );
}

export default App;