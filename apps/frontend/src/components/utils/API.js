import axios from "axios";

const PORT = "http://localhost:8080";

export default {
    // Get all Cats
    getCats: function() {
      return axios.get(PORT + '/cats/catslist/');
    },
    // Get the cat with given id
    getCat: function(id){
        return axios.get(PORT + '/cats/api/cats/' + id);
    },
    // Save new lost cat
    saveCat: function(catData){
        return axios.post(PORT + "/cats/catslist", catData);
    }
};