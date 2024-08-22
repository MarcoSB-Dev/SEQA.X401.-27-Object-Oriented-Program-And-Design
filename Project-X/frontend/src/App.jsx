import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [message, setMessage] = useState('');

    const pingBackend = () => {
        axios.get('http://localhost:4000/ping/') // Use the full URL
            .then(response => {
                console.log('Response data:', response.data); // Log the entire response data
                if (response.data && response.data.message) {
                    setMessage(response.data.message);
                    console.log('Message:', response.data.message);
                } else {
                    console.error('Message field is missing in the response');
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    };

    return (
        <div>
            <button onClick={pingBackend}>Ping</button>
            <p>{message}</p>
        </div>
    );
};

export default App;