import axios from "axios";

const URL = process.env.REACT_APP_URL_ROOT;

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
        return axios.post(URL + "/cats/catslist", catData);
    }
};