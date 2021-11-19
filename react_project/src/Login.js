import React, {Component} from 'react';
import './Login.css';


class Login extends Component {
   render(){
      return(
      <div className="Login">
        <form method="post">
           ID<br></br>
           <input type="text"/><br></br>
           PW<br></br>
           <input type="password"/><br></br><br></br>
           <input type="submit" value="로그인"/>
			<br></br>
           <input type="submit" value={"회원가입"}/>

        </form>




      </div>
      );
   }

}



export default Login;
