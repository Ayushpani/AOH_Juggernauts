import './App.css';
import { Link } from 'react-router-dom'; // Import Link from react-router-dom

function App() {
  return (
    <div className="App">
      <nav>
        <div className="logo">Logo</div>
        <ul className="nav-links">
          <li><a href="#">Home</a></li>
          <li><a href="About.html">About</a></li>
          <li><a href="/audiotable">Contact</a></li>
          <li><Link to="/login">Login</Link></li> 
        </ul>
      </nav>

      <div className="content">
        <h1>Pro-Connect</h1>
        <p>
          Our cutting-edge web application employs automated call quality monitoring, leveraging advanced machine learning and speech processing techniques to optimize customer interactions. By providing objective feedback and comprehensive call summaries, we enhance customer satisfaction and drive operational excellence in call center performance.
        </p>
      </div>
    </div>
  );
}

export default App;
