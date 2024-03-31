import React from 'react';
import { Link } from 'react-router-dom';

function Registration() {
  return (
    <div className="registration-container">
      <h2>Register</h2>
      {/* Registration form */}
      <form>
        {/* Form fields */}
        <input type="text" placeholder="Username" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <input type="password" placeholder="Confirm Password" />
        {/* Register button */}
        <button type="submit">Register</button>
      </form>
      {/* Link to Login page */}
      <p>Already have an account? <Link to="/login">Login</Link></p>
    </div>
  );
}

export default Registration;
