import React, { useState } from 'react';
import './CategoriesMenu.css';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';



function CategoryDropdown({ categoryTitle, categoryElements }) {
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
                {elements}
            </DropdownButton>
        </div>
    );
}


const CategoriesMenu = () => {
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
            {sections}
        </div>
    );
}


export default CategoriesMenu;