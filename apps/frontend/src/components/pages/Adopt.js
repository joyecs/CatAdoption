// import { render } from "@testing-library/react";
import React, { Component } from "react";
import CatCard from "../CatCard";
import { Link } from "react-router-dom";
import API from "../utils/API";

class Adopt extends Component{

    state = {
        results:[]
    };

    componentDidMount(){
        this.loadCats();
    }

    loadCats = () => {
        API.getCats()
        //   .then(res => console.log(res.data.cats))
          .then(res => this.setState({ results: res.data.cats }))
          .catch(err => console.log(err));
    };

    render(){
        return (
            <div id="main-wrapper">
                <div className="container">
                    <div className="row">
                        <div className="col-6">
                            <h3>Available</h3>
                        </div>
                        <div className="col-6">
                            <h4>Found a lost kitty? Post Here!</h4>
                            <Link to="/postlostcat">
                                <button>
                                    Post New Lost Kitty
                                </button>
                            </Link>
                        </div>
                    </div>
                    <hr />
                    <div className="row gtr-200">
                        {this.state.results.map(cat => (
                            <CatCard 
                                key={cat.id}
                                id={cat.id}
                                breed={cat.breed}
                                age={cat.age}
                                color={cat.color}
                                image={cat.image}
                            />
                        ))}
                    </div>
                </div>
            </div>
        );
    }
}
export default Adopt;