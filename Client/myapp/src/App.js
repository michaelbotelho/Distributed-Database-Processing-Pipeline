import logo from './logo.svg';
import './App.css';


function FsiltersTable({ categories }) {
  const rows = [];

  categories.forEach(category => {
    document.writeln(category);
    
    //rows.push(
    //  <CategoryHeader header={entryHeader}/>
    //);
    //
    //for (let index = 0; index < entryData.length; index++) {
    //  const data = entryData[index];
    //  rows.push(
    //    <CategoryData data={data}/>
    //  );
    //}
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Categories</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function CategoryHeaderRow( { header }) {
  return(
    <tr>
      <th>{header}</th>
    </tr>
  );
}

function CategoryDataRow( { data }) {
  return(
    <tr>
      <td>{data}</td>
    </tr>
  );
}


function FiltersTable({ categories }) {
  const rows = [];

  for (var category in categories) {
    var categoryData = categories[category];
    
    rows.push(
      <CategoryHeaderRow header={category} />
    );

      categoryData.forEach(element => {
        rows.push(
          <CategoryDataRow data={element}/>
        );
      })

  }

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Categories</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  );
}


export default function App() {
  var sports = ["Soccer", "Football", "Baseball", "Basketball", "Hockey"];
  var countries = ["Canada", "USA", "Germany", "China", "France", "Spain"];
  const CATEGORIES = {
    Sports: sports, 
    Countries: countries
  };

  for (let index = 0; index < CATEGORIES.length; index++) {
    const element = CATEGORIES[index];
    
  }
  return <FiltersTable categories={CATEGORIES} />
}
