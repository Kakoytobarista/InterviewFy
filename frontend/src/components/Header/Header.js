import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  return (
    <div className="header">
      <Link to="/" className="logo"> {}
        <span className="white-text">Interview</span>
        <span className="black-text">Fy</span>
      </Link>
      <nav className="nav-links">
        <Link to="/interview/constructor" className="nav-link">Interview Constructor</Link>
        <Link to="/interview/select" className="nav-link">Interview Select</Link>
      </nav>
    </div>
  );
};

export default Header;
