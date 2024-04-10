import React from "react";

const Event = ({ event }) => {
    return (
        <div className="event-container">
            <h6 id="event_name">{event['event_name']}</h6>
            <p id="sport">{event['sport']}</p>
            <p id="location">{event['locality']} - {event['country']}</p>
            <p id="date">{event['date']}</p>
        </div>
    );
}

export default Event;