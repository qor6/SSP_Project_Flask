import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Login from './signUp/Login';
import SignUp from './signUp/SignUp';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <nav>
            <ul>
              <div>
                <Link to="./signUp/Login.js">Login</Link>
              </div>
              <div>
                <Link to="./SignUp.js">SignUp</Link>
              </div>
            </ul>
          </nav>
          <Routes>
            <Route path='/' component={Login}/>
            <Route path='./SignUp' component={SignUp}/>
          </Routes>
        </div>
      </Router>
    );
  }
}

export default App;
