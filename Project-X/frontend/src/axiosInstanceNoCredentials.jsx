import axios from 'axios';

// Create an Axios instance without credentials
const axiosInstanceNoCredentials = axios.create({
  baseURL: 'https://fakestoreapi.com',
});

export default axiosInstanceNoCredentials;