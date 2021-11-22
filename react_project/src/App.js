import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Login from './Login_Signup/Login';
import SignUp from './Login_Signup/SignUp';
  /* <div>
                <Link to="./Login_Signup/Login.js">Login</Link>
              </div>
              <div>
                <Link to="./SignUp.js">SignUp</Link>
              </div>*/
class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <nav>
            <ul>
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
