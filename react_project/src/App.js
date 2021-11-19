import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Login from './Login';
import SignUp from './SignUp';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <nav>
            <ul>
              <div>
                <Link to="C:\Users\mom42\PycharmProjects\SSP_Project_React/src/Login.js">Login</Link>
              </div>
              <div>
                <Link to="C:\Users\mom42\PycharmProjects\SSP_Project_React/src/SignUp.js">SignUp</Link>
              </div>
            </ul>
          </nav>
          <Routes>
            <Route path='C:\Users\mom42\PycharmProjects\SSP_Project_React/src/Login.js' component={Login}/>
            <Route path='C:\Users\mom42\PycharmProjects\SSP_Project_React/src/SignUp.js' component={SignUp}/>
          </Routes>
        </div>
      </Router>
    );
  }
}

export default App;
