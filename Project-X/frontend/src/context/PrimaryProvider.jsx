// Project-X/frontend/src/context/PrimaryProvider.jsx
import React, { createContext, useState } from 'react';

export const PrimaryContext = createContext();

const PrimaryProvider = ({ children }) => {
    const [state, setState] = useState(null);

    return (
        <PrimaryContext.Provider value={{ state, setState }}>
            {children}
        </PrimaryContext.Provider>
    );
};

export default PrimaryProvider;