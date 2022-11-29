
<template>
     <footer class="footer style-4">
        <div class="footer__top">
            <div class="container">
                <div class="row">
                    <div class="col-md-6">
                        <div class="content-left">
                            <h3 class="fs-22">{{title}}</h3>
                            <p class="fs-20">{{desc}}</p>
                            <ul class="list-info">
                                <li> <span class="icon-message"></span>{{mail}}</li>
                                <li><span class="icon-Calling"></span>{{phone}}</li>
                            </ul>
                            <ul class="list-social">
                                <li><span class="icon-twitter"></span></li>
                                <li><span class="icon-facebook"></span></li>
                                <li><span class="icon-place"></span></li>
                                <li><span class="icon-youtobe"></span></li>
                                <li><span class="icon-tiktok"></span></li>
                                <li><span class="icon-reddit"></span></li>
                            </ul>
                            
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="content-right">
                            <form v-on:submit="sendForm">
                                <div class="form row">
                                    <div class="form-group col-md-6">
                                        <label>Your Name</label>
                                        <input  v-model="ContactForm.name" type="text" class="form-control" placeholder="Type your name here" />
                                    </div>
                                    <div class="form-group col-md-6">
                                        <label>Your Email</label>
                                        <input type="email" v-model="ContactForm.email" class="form-control" id="exampleInputEmail" placeholder="Type your email here" />
                                    </div>
                                    <div class="form-group col-md-12">
                                        <label class="mb-6">Your Message</label>
                                        <textarea v-model="ContactForm.message" placeholder="Leave your question or comment here"></textarea>
                                    </div>
                                </div>
                                <button type="submit" class="btn-action style-4"><span>SUBMIT YOUR MESSAGE</span></button>
                              </form>
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer__bottom">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <p>© 2022. All rights reserved by <a href="https://quiobot.com">{{author}}</a></p>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>

import "./styles.scss";
import axios from 'axios'

const querystring = require("querystring");
export default {

    name: "Feature",
     data (){
        return {
            sent: false,
            ContactForm: {
                name: '',
                email: '',
                subject: 'Website Message',
                message: ''
              },
            title: 'Contact Us',
            desc : 'We are always open and we welcome and questions you have for our team. If you wish to get in touch, please fill out the form below. Someone from our team will get back to you shortly',
            mail: 'Contact@quiobot.com',
            phone : '+212 697856535',
            author : 'QuioBot',
        }    
    },
    methods: {
            sendForm(e) {
              e.preventDefault()
              console.log(this.ContactForm)
              axios.post('https://quioapi.000webhostapp.com/mail_server.php',
              querystring.stringify(this.ContactForm)).then(() => {
                this.sent = true
              })
            }
          }
};
</script>
            
            