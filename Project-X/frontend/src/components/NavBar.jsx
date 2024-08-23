import React from 'react';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <a href="/">MyApp</a>
      </div>
      <ul className="navbar-links">
        <li><a href="/">Home</a></li>
        <li><a href="/about">Category</a></li>
        <li><a href="/contact">Cart</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;