
<template>
    <section className='mobie-pb0'>
        <div className="banner-top style-8">
            <div className="container">
            <div className="row">
                <div className="col-xl-6 col-md-12">
                    <div className="banner-top__content">
                        <h6  style="font-size: 4em; color:#42ccce;" class="sub-title">{{subtitle}}</h6>
                        <h2 style="font-size: 5em;" className="title">{{title}}</h2>
                        <p className="desc">{{desc}}</p>
                        <a class="btn-action style-5" href="#">
                                <span>Github Repository</span>
                        </a>
                    </div>
                </div>
                <div className="col-xl-6 col-md-12">
                    <div className="banner-top__image">
                        <ChatBot msg="Welcome to Your Vue.js App"/>
                    </div>
                </div>
            </div>
            </div>
        </div>
        <div className="banner-top__main">
                <div className="container">
                        <div className="row">
                            <div className="col-12">
                                <div className="banner-top__sale">
                                
                                    <!-- <div className="countdown">
                                        <p className="fs-17">Token sale End In!</p>
                                        <Countdown 
                                            starttime="Jul 1, 2022 15:37:25" 
                                            endtime="Dec 8, 2022 16:37:25" >
                                        </Countdown>
                                    </div> -->
                                    
                                        <div className="token-bar">
                                            <div className="top">
                                                <h6>Raised - <span>15,000 Dataset</span></h6>
                                                <h6>Target - <span>1,500,000 Dataset</span></h6>
                                            </div>
                                            <div className="main">
                                                <div className="progress-token">
                                                    <p className="fs-14">23,390</p>
                                                </div>
                                            </div>

                                            <!-- <div className="bottom">
                                                <p className="fs-14">Soft cap</p>
                                                <p className="fs-14">Crowdsale</p>
                                                <p className="fs-14">Hard cap</p>
                                            </div> -->
                                        </div>

                                        <!-- <ul className="list-coin">
                                            <li><span className="icon-bitcoin"></span></li>
                                            <li><span className="icon-coinp"></span></li>
                                            <li><span className="icon-coinp"></span></li>
                                            <li><span className="icon-kyber-network"></span></li>
                                        </ul> -->
                                </div>
                            </div>
                        </div>
                    </div>                
        </div>
    </section>
</template>

<script>
// import Countdown from '../Layouts/Countdown.vue';
import "./styles.scss";
import { dataBanner } from '../../fake-data/databanner';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import '../../App.css';
import ChatBot from '../Chatbot/ChatBot.vue'

export default {
    name: "About",
     components: {
        // Countdown,
        ChatBot,
    },
    data (){
        return {
            dataBanner,
            subtitle : 'BERT And GPT',
            title : 'Quiobot Chat Bot',
            desc : ' Quiobot chatbot is AI-powered conversational solutions that help patients, insurance companies, and healthcare providers easily connect with each other.',
        }    
    }
};
</script>
            
            