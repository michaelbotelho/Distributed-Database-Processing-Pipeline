import React from 'react';

function Slider({ sliderValue, onChange }) {
    return (
        <div>
            <input
                type="range"
                min="1"
                max="10"
                defaultValue={sliderValue}
                onChange={onChange}
            />
            <p>Weeks: {sliderValue}</p>
        </div>
    );
}

export default Slider;