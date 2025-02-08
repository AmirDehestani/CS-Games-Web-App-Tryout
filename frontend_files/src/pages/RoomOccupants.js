import React, { useState } from 'react';
import axios from 'axios';

const RoomOccupants = () => {
    const [room, setRoom] = useState('');
    const [date, setDate] = useState('');
    const [occupants, setOccupants] = useState(null);

    const searchOccupants = async () => {
        const res = await axios.get(
            'http://127.0.0.1:5000/api/check-occupants',
            {
                params: {
                    room_number: room,
                    date: date,
                },
            }
        );
        setOccupants(res);
    };

    return (
        <>
            <h1>Check your Room Occupants here:</h1>
            Room:{' '}
            <input
                type="text"
                value={room}
                onChange={(event) => setRoom(event.target.value)}
            ></input>
            Date:{' '}
            <input
                type="date"
                value={date}
                onChange={(event) => setDate(event.target.value)}
            ></input>
            <button onClick={() => searchOccupants()}>Search</button>
            <div>
                {occupants
                    ? `room type: ${occupants.room_type}
                price per night: ${occupants.price_per_night}
                air conditioning: ${
                    occupants.extras.air_conditioning ? 'yes' : 'no'
                }
                jacuzzi: ${occupants.extras.jacuzzi ? 'yes' : 'no'}
                mini bar: ${occupants.extras.mini_bar ? 'yes' : 'no'}
                wifi: ${occupants.extras.wifi ? 'yes' : 'no'}`
                    : 'No occupied room found at the specified date'}
            </div>
        </>
    );
};

export default RoomOccupants;
