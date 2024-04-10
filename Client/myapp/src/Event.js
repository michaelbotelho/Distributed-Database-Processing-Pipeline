import React from "react";
import './Event.css'

function Event({ event_name, sport, country, locality, date }) {
    return (
        <div className="event-container">
            <section>
                <h6 id="event_name">{event_name}</h6>
                <p id="sport">{sport}</p>
            </section>
            <section>
                <p id="location">{locality} - {country}</p>
                <p id="date">{date}</p>
            </section>
        </div>
    );
}

export default Event;