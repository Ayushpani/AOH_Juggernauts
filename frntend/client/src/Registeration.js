import React from 'react';
import { Link } from 'react-router-dom';
import './Register.css'
function Registration() {
  return (
    <div className="reg-cont">
    <div className="registration-container">
      <h2>Register</h2>
       <form>
        
        <input type="text" placeholder="Username" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <input type="password" placeholder="Confirm Password" />
        
        <button type="submit">Register</button>
      </form>
      
      <p>Already have an account? <Link to="/login">Login</Link></p>
    </div>
    </div>
  );
}

export default Registration;
