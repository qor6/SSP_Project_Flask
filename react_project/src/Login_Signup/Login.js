//import { Link } from 'react-router-dom';
import React, {Component} from 'react';
import './Login.css';

class Login extends Component {
   render(){
      return(
      <div className="Login">
         <h1>SSP</h1>
        <form method="post">
           ID<br></br>
           <input type="text"/><br></br>
           PW<br></br>
           <input type="password"/><br></br><br></br>
           <input type="submit" value={"로그인"}/>
        </form>
      </div>
      );
   }
}

export default Login;
