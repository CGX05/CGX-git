import axios from "axios";

const request = axios.create({
  baseURL: "http://8.134.127.43:8000",
  timeout: 5000,
});

// 请求拦截器
request.interceptors.request.use(
  config => {
    // 添加token
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default request;
