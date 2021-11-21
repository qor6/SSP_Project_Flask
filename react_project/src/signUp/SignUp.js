import React, {Component} from 'react';
import './SignUp.css';


class SignUp extends Component {
	render(){
		return(
		<div className="SignUp">
		  <form method="post">
			  <p>
				Name<br></br>
              	<input type="text"/><br></br><br></br>
			    Nickname<br></br>
          		<input type="text"/><br></br><br></br>
			    ID<br></br>
          		<input type="text"/><br></br><br></br>
			    Password<br></br>
          		<input type="password"/><br></br><br></br>
			    Re-enter password<br></br>
          		<input type="password"/><br></br><br></br>
			  </p><br></br>
			  <center><input type="submit" value="회원가입"/></center>
		  </form>
		</div>
		);
	}


}



export default SignUp;