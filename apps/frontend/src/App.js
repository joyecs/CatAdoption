// import logo from './logo.svg';
import { BrowserRouter as Router, Route } from "react-router-dom";
import TopNav from "./components/TopNav";
import Home from "./components/pages/Home";
import Adopt from "./components/pages/Adopt";
import Donate from "./components/pages/Donate";
import Volunteer from "./components/pages/Volunteer";
import Footer from "./components/Footer";
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <TopNav />
        <Route exact path="/" component={Home} />
        <Route exact path="/adopt" component={Adopt} />
        <Route exact path="/donate" component={Donate} />
        <Route exact path="/volunteer" component={Volunteer} />
        <Footer />
      </div>
    </Router>
  );
}

export default App;
