<template>

        <header :class="['header style-4', { 'is-fixed': isSticky }]" id="header_main">
     
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="header__body">
                        <div class="header__logo">
                            <a href="#Home">
                                <img id="site-logo" src="../../assets/images/logo/logo-05.png" data-retina="assets/images/logo/logo-main@x2.png" data-width="165" data-height="40">
                            </a>
                        </div>
                        <div class="header__right">
                            <nav id="main-nav" class="main-nav" v-bind:class="{active: isActive}">
                                <ul id="menu-primary-menu" class="menu">
                                    
                                    
                                    <li class="menu-item">
                                        <a class="page-scroll" href="#Home">Home</a>
                                    </li>

                                    <li class="menu-item">
                                        <a class="page-scroll" href="#RoadMap">Road Map</a>
                                    </li>

                                    <li class="menu-item">
                                        <a class="page-scroll" href="#Technologies">Technologies</a>
                                    </li>
                                    <!-- <li class="menu-item">
                                        <a class="page-scroll" href="#About As">About As</a>
                                    </li> -->
                                    <li class="menu-item">
                                        <a class="page-scroll" href="#Training">Training</a>
                                    </li>
                                    <li class="menu-item">
                                        <a class="page-scroll" href="#FAQ">FAQ</a>
                                    </li>
                                    <li class="menu-item">
                                        <a class="page-scroll" href="#Contact">Contact</a>
                                    </li>
                                    <!-- <li class="menu-item">
                                        <a class="page-scroll" href="#Subscribe">Subscribe</a>
                                    </li> -->
                                   
                                   
                                </ul>
                            </nav>
                            <div class="group-button">
                                <!-- <a class="btn-action style-5" href="/sign-in"><span class="effect">Log in</span></a> -->

                            </div>
                             <div class="mobile-button" @click="toggleActive()" v-bind:class="{active: isActive}" ><span></span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        </header>  

</template>

<script>

import "./styles.scss";

export default {
    name: "Header",
    data() {
        return {
            isSticky: false,
            isActive: false,
            isActiveMobile:false,
            isActiveMobile1:false,
            isActiveMobile2:false,
            isActiveMobile3:false,
            isActiveMobile4:false,
            isActiveMobile5:false,
            search: false,
            Header: null,
            HeaderImg: null
        };
    },
    mounted() {
        const that = this;
        window.addEventListener("scroll", () => {
            let scrollPos = window.scrollY;
            if (scrollPos >= 100) {
                that.isSticky = true;
            } else {
                that.isSticky = false;
            }
        });
    },
    methods: {
        isSideMenuMethod(isSideMenu){
            return this.isSideMenu = !isSideMenu
        },
        toggleActive(){
            this.isActive = !this.isActive;
        },
        toggleActiveMobile(){
            this.isActiveMobile = !this.isActiveMobile;
        },
        toggleActiveMobile1(){
            this.isActiveMobile1 = !this.isActiveMobile1;
        },
        toggleActiveMobile2(){
            this.isActiveMobile2 = !this.isActiveMobile2;
        },
        toggleActiveMobile3(){
            this.isActiveMobile3 = !this.isActiveMobile3;
        },
        toggleActiveMobile4(){
            this.isActiveMobile4 = !this.isActiveMobile4;
        },
        toggleActiveMobile5(){
            this.isActiveMobile5 = !this.isActiveMobile5;
        },
         toggleActiveSearch(){
            this.search = !this.search;
        },
    },
};
</script>
