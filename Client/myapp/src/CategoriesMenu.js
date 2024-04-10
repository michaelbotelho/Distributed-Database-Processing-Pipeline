import React, { useState } from 'react';
import './CategoriesMenu.css';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Slider from './Slider';



function CategoryDropdown({ categoryTitle, categoryElements }) {
    const [isHovered, setIsHovered] = useState(false);

    const handleHover = () => {
        setIsHovered(!isHovered);
    };

    const elements = [];

    categoryElements.forEach(element => {
        elements.push(
            <div id="dropdown-item" key={element}>
                <input type="checkbox" name={categoryTitle} value={element}></input>
                <label for={categoryTitle}>{element}</label><br></br>
            </div>
            //<Dropdown.Item id="dropdown-item" key={element} href={"#/" + categoryTitle + "/" + element}>{element}</Dropdown.Item>
        );
    });

    return (
        <div onMouseEnter={handleHover} onMouseLeave={handleHover}>
            <DropdownButton id="dropdown-button" title={categoryTitle} show={isHovered}>
                {elements}
            </DropdownButton>
        </div>
    );
}


function CategoriesMenu({ sliderValue, onSliderChange, onSubmit }) {
    // These sections will eventually be replaced by dynamic information form cache service
    var sports = ["Soccer", "Football", "Baseball", "Basketball", "Hockey"];
    var countries = ["Canada", "USA", "Germany", "China", "France", "Spain"];
    const CATEGORIES = {
        Sports: sports,
        Countries: countries
    };

    const sections = [];

    for (var category in CATEGORIES) {
        sections.push(
            <CategoryDropdown key={category} categoryTitle={category} categoryElements={CATEGORIES[category]} />
        );
    }

    return (
        <div className="categories-menu">
            <Slider id="weeks-slider" value={String(sliderValue)} onChange={onSliderChange} />
            <button onClick={onSubmit}>Search</button>
            {sections}
        </div>
    );
}


export default CategoriesMenu;