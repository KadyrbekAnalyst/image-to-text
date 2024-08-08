import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Welcome to the Image Creator!</h1>
      <p>Generate your custom designs and print them on T-shirts or hoodies.</p>
      <Link to="/create-image">
        <button style={{ padding: '10px 20px', fontSize: '16px' }}>Create Your Design</button>
      </Link>
    </div>
  );
};

export default HomePage;
