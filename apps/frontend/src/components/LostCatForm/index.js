import React, { Component } from "react";
import API from "../utils/API";

class LostCatForm extends Component {
    state = {
        breed: "",
        age: "",
        color: "",
        image: null
    }
    //handle select image on pop up
    onFileChange = event =>{
        this.setState({
            selectedFile: event.target.files[0]
        });
    }
    //handle file upload

    handleInputChange = event => {
        const { name, value } = event.target;
        this.setState({
            [name]: value
        });
    };

    handleFormSubmit = event => {
        event.preventDefault();
        if (this.state.breed && this.state.age) {
            const formData = new FormData();
            formData.append(
                'breed',this.state.breed
            )
            formData.append(
                'age',this.state.age
            )
            formData.append(
                'color',this.state.color
            )
            formData.append(
                'image',this.state.selectedFile
            )
            API.saveCat(formData).catch(err => console.log(err));
            // API.saveCat({
            //     breed: this.state.breed,
            //     age: this.state.age,
            //     color: this.state.color,
            //     image: this.state.image
            // }).catch(err => console.log(err));
        }
    };

    render() {
        return (
            <div id="main-wrapper">
                <div className="container">
                    <h3>Post New Lost Cat Form</h3>
                    <form>
                        <input
                            value={this.state.breed}
                            name="breed"
                            onChange={this.handleInputChange}
                            type="text"
                            placeholder="Breed"
                        />
                        <input
                            value={this.state.age}
                            name="age"
                            onChange={this.handleInputChange}
                            type="text"
                            placeholder="Age"
                        />
                        <input
                            value={this.state.color}
                            name="color"
                            onChange={this.handleInputChange}
                            type="text"
                            placeholder="Color"
                        />
                        <input
                            value={this.state.lastName}
                            name="image"
                            onChange={this.onFileChange}
                            type="file"
                            placeholder="Cover Pic"
                        />
                        <button style={{ float: "right" }} onClick={this.handleFormSubmit}>Submit</button>
                    </form>
                </div>
            </div>
        );
    }
}

export default LostCatForm;