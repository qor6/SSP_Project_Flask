import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './Apxp';
import reportWebVitals from './etc/reportWebVitals';
import Login from './signUp/Login';
import SignUp from './signUp/SignUp';

// eslint-disable-next-line
let element = ReactDOM.render(
  <React.StrictMode>
      <App />
      <Login/>
      <SignUp/>
  </React.StrictMode>,
   document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
