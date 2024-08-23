import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:4000/', // Base URL of your Python server
  withCredentials: true, // Ensure cookies are sent with requests
});

// Remove the CSRF token interceptor
axiosInstance.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default axiosInstance;