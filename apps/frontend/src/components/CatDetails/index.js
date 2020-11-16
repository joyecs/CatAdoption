import React, {Component} from "react";
import API from "../utils/API";

class CatDetails extends Component{
    state = {
        cat:{}
    }

    componentDidMount(){
        API.getCat(this.props.match.params.id)
        // .then(res => console.log(res.data))
        .then(res => this.setState({ cat: res.data }))
        .catch(err => console.log(err));
    }

    render(){
        return(
            <div id="main-wrapper">
                <div className="container">
                    <h3>Cat Details
                        <span>
                            <button style={{float: 'right'}}>EDIT DETAILS</button>
                        </span>
                    </h3>
                    <br />
                    <div className="row">
                        <div className="col-7">
                            <img src={this.state.cat.image} alt="" className="img-index"/>
                        </div>
                        <div className="col-5">
                            <p>Breed: {this.state.cat.breed}</p>
                            <p>Color: {this.state.cat.color}</p>
                            <p>Age: {this.state.cat.age}</p>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
};

export default CatDetails;