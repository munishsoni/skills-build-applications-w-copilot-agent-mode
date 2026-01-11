
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import logo from './logo.svg'; // Replace with './octofitapp-small.png' if available


function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark">
        <div className="container-fluid octofit-logo">
          <a className="navbar-brand d-flex align-items-center" href="#">
            <img src={logo} alt="OctoFit Logo" style={{height: 40, marginRight: 12}} />
            <span>OctoFit Tracker</span>
          </a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item"><a className="nav-link" href="#">Home</a></li>
              <li className="nav-item"><a className="nav-link" href="#teams">Teams</a></li>
              <li className="nav-item"><a className="nav-link" href="#activities">Activities</a></li>
              <li className="nav-item"><a className="nav-link" href="#workouts">Workouts</a></li>
              <li className="nav-item"><a className="nav-link" href="#leaderboard">Leaderboard</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container mt-5">
        <div className="card p-4">
          <h1 className="mb-4">Welcome to OctoFit Tracker</h1>
          <p className="lead">Track your fitness, join teams, and compete on the leaderboard!</p>
          <a className="btn btn-primary mt-3" href="#get-started">Get Started</a>
        </div>
      </div>
    </div>
  );
}

export default App;
