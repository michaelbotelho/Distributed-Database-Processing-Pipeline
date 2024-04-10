import React from 'react';

function Slider({ value, onChange }) {
    return (
        <div>
            {/* Render the slider input element */}
            <input
                type="range"
                min="1"
                max="10"
                value={value}
                onChange={onChange}
            />
            {/* Display the current value of the slider */}
            <p>Weeks: {String(value)}</p>
        </div>
    );
}

export default Slider;