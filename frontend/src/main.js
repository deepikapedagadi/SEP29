import { createApp } from 'vue'
//import './style.css'
import App from './App.vue'
import router from "./router";
//import API from './services/api';


//const app = createApp(App);
//app.use(router);
createApp(App).use(router).mount('#app')



//main.js is an entry point where it initializes vue app and router 