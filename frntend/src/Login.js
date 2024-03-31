import React from 'react';
import { Link } from 'react-router-dom';

function Login() {
  return (
    <div className="login-container">
      <h2>Login</h2>
      {/* Login form */}
      <form>
        {/* Form fields */}
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        {/* Login button */}
        <button type="submit">Login</button>
      </form>
      {/* Link to Registration page */}
      <p>Don't have an account? <Link to="/register">Register</Link></p>
    </div>
  );
}

export default Login;
