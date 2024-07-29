import axios from "axios";
import { DefaultHost } from "../service/valueDefault";
import { getCsrfToken } from "../service/token";

let refresh = false
// let isRefreshing = false;
// let failedQueue = [];

// // 用于refresh前的api请求，在refresh之后会重新发送这些请求
// const processQueue = (error, token = null) => {
//     failedQueue.forEach(prom => {
//         if (error) {
//             prom.reject(error);
//         } else {
//             prom.resolve(token);
//         }
//     });

//     failedQueue = [];
// };

// api请求之前，检测access token是否过期
axios.interceptors.request.use(
    async (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// 当返回401错误时，尝试用refresh_token请求新的access_token
axios.interceptors.response.use(resp => resp, async error => {
    const refreshToken = localStorage.getItem('refresh_token');
    const originalRequest = error.config;

    // 错误码为401，有refreshToken且还未进行重试时
    if (error.response.status === 401 && refreshToken && !refresh) {
        console.log('token not valid')
        refresh = true;
        // if (isRefreshing) {
        //     return new Promise(function (resolve, reject) {
        //         failedQueue.push({ resolve, reject });
        //     }).then(token => {
        //         originalRequest.headers['Authorization'] = 'Bearer ' + token;
        //         return axios(originalRequest);
        //     }).catch(err => {
        //         return Promise.reject(err);
        //     });
        // }

        // 用于锁定refresh，避免多个api请求失败导致的多次refresh
        originalRequest._retry = true;
        // isRefreshing = true;

        try {
            const response = await axios.post(DefaultHost + 'api/token/refresh/', {
                refresh: refreshToken
            }, {
                headers: {
                    'X-CSRFToken': getCsrfToken(),
                    'Content-Type': 'application/json'
                }
            });
            // console.log(response)
            if (response.status === 200) {
                axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
                localStorage.setItem('access_token', response.data.access);
                localStorage.setItem('refresh_token', response.data.refresh);
                // processQueue(null, response.data.access);
                window.location.href = '/pos/home';
                return axios(originalRequest);
            }
        } catch (err) {
            console.log(err)
            // processQueue(err, null);
            console.error('Refresh token is invalid', err);
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            window.location.href = '/login';  // Redirect to login page
        } finally {
            // isRefreshing = false;
            refresh = false;
        }
    }

    return Promise.reject(error);
});





// axios.interceptors.response.use(resp => resp, async error => {
//     const refreshToken = localStorage.getItem('refresh_token');
//     if (error.response.status === 401 && refreshToken && !refresh) {
//         refresh = true;
//         try{
//             const response = await axios.post(DefaultHost+'api/token/refresh/', {
//                 refresh:refreshToken
//             }, 
//             {
//                 headers:{
//                     'X-CSRFToken': getCsrfToken(), 
//                     'Content-Type': 'application/json'
//                 }
//             });
//             console.log('response:', response)
//             if (response.status === 200) {
//                 axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
//                 localStorage.setItem('access_token', response.data.access);
//                 localStorage.setItem('refresh_token', response.data.refresh);
//                 return axios(error.config);
//             }
//         }catch(err){
//             console.error('Refresh token is invalid', err);
//             localStorage.removeItem('access_token');
//             localStorage.removeItem('refresh_token');
//             window.location.href = '/login';  // Redirect to login page
//         }
//     }
//     refresh = false;
//     // return error;
//     return Promise.reject(error)
// });