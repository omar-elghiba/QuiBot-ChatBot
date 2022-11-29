import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import Toaster from "@meforma/vue-toaster";
import AOS from "aos";
import "aos/dist/aos.css";

import "./assets/css/font-awesome.css";
import "./assets/css/bootstrap.css";
import "./assets/css/ntfs.css";
import "./assets/App.scss";

const app = createApp(App).use(router).use(Toaster);

app.use(AOS.init).mount("#app");

