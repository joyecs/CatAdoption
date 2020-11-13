import React, {Component} from 'react'
import './App.css';
​
class Like extends Component{
  constructor(){
    super();
    this.state = {
      liked: false,
      buttonStyle: {
        color: 'red',
        fontSize: "150px",
      },
    }
  }//end of constructor
  clicked(){
    let bs = {...this.state.buttonStyle};
    bs.color = this.state.liked? "red" : "green";
    this.setState({
      liked: !this.state.liked,
      buttonStyle: bs,
    });
  }
  render(){
    let cls = this;
    let text_ = "";
    if (this.state.liked) text_ = 'you have liked it'
    else text_ = "";
    return (
      <div>
        <p>this.state.liked: {this.state.liked.toString()}</p>
        <button style={this.state.buttonStyle} onClick={function(){cls.clicked();}}>
          {this.state.liked === true? 'liked': 'like it'}
        </button>
        <p>{text_}</p>
      </div>
    )
  }//end of render
}//end of Like
class Remote extends Component{
  constructor(){
    super();
    this.state = {
      user_email: 'Unknown',
    }
  }
  componentDidMount(){
    let cls = this;
    const username = 'Pikicode'
    let url = "https://api.github.com/users/" + username;
    fetch(url).then(res=>res.json()).then(function(res){
      console.log(res);
      cls.setState({
        user_email: res.email,
      });
    });
  }//end of componentdidmount
  render(){
    return (
      <div>
        <p>Get user's public email from api.github.com/users/xxxxx</p>
        <p>
          user name: Pikicode ---
          user_email: {this.state.user_email}
        </p>
      </div>
    )
  }
}//end of remote
function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <Like></Like>
        <Remote></Remote>
      </header>
    </div>
  );
}
​
export default App;