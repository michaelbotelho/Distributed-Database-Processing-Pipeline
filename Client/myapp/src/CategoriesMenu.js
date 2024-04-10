import React, { useState } from 'react';
import './CategoriesMenu.css';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Slider from './Slider';



function CategoryDropdown({ categoryTitle, categoryElements}) {
    const [isHovered, setIsHovered] = useState(false);

    const handleHover = () => {
        setIsHovered(!isHovered);
    };

    const elements = [];

    categoryElements.forEach(element => {
        elements.push(
            <Dropdown.Item id="dropdown-item" key={element} href={"#/" + categoryTitle + "/" + element}>{element}</Dropdown.Item>
        );
    });

    return (
        <div onMouseEnter={handleHover} onMouseLeave={handleHover}>
            <DropdownButton id="dropdown-button" title={categoryTitle} show={isHovered}>
                {categoryElements.map(option => (
                    <Dropdown.Item id="dropdown-item" key={option} value={option}>{option}</Dropdown.Item>
                ))}
            </DropdownButton>
        </div>
    );
}


function CategoriesMenu({ sliderValue, onClickSearch, onSliderChange, onInputChange1, onInputChange2 }) {
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
            <CategoryDropdown 
                categoryTitle={category} 
                categoryElements={CATEGORIES[category]}
            />
        );
    }

    return (
        // <div className="categories-menu">
        //     <Slider sliderValue={sliderValue} onChange={onSliderChange} />
        //     <button onClick={onClickSearch}>Search</button>
        //     {sections}
        // </div>
        <div className="categories-menu">
            <Slider id="weeks-slider" sliderValue={sliderValue} onChange={onSliderChange} />
            <button onClick={onClickSearch}>Search</button>
        </div>
    );
}


export default CategoriesMenu;