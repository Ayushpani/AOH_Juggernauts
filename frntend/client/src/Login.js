import React from 'react';
import { Link } from 'react-router-dom';
import './Login.css'
function Login() {
  return (
    <div className="login-container">
      <h2>Login</h2>
      
      <form>
        
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        
        <button type="submit">
        <Link to='/audiotable'>Login</Link></button>
      </form>
      
    </div>
  );
}

export default Login;
