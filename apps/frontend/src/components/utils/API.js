import axios from "axios";

const URL = process.env.REACT_APP_URL_ROOT;
// handle csrf tokens in React/Axios
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
const PORT = "http://localhost:8080";

export default {
    // Get all Cats
    getCats: function() {
      return axios.get(URL + '/cats/catslist/');
    },
    // Get the cat with given id
    getCat: function(id){
        return axios.get(URL + '/cats/api/cats/' + id);
    },
    // Save new lost cat
    saveCat: function(catData){
        return axios.post(PORT + "/cats/catslist/", catData);
    }
};