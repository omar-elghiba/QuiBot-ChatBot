<template>

<div style="height: 450px; width: 90%;"  class="card">
    <div class="card-header msg_head">
      <div class="d-flex bd-highlight">
        <div class="img_cont">
          <img src="../../assets/images/logo/chatbot.png" class="rounded-circle user_img">
          <span class="online_icon"></span>
        </div>
        <div class="user_info">
          <span>Quiobot Chat Bot</span>
          <p>Powered By Omar El Ghiba</p>
        </div>
      
      </div>
    </div>

    <!-- ---------------------------------------------------------------------- -->



    <div class="card-body msg_card_body">


        <div v-show="elementVisible" ref="chatbox">
      <ul class="chat-box-list">
        <li
        class="message"
          
        >
        <div>
                <img src="https://i.postimg.cc/vBVgY5GH/Untitled-design-11.png" style="height: 40px; width: 40px ;float: left;">
        </div>
          <p >
            <span style="padding: 8px;
                          color: white;
                          border-radius: 4px;
                          /* background: #000; */
                          ">{{ welcome }}</span>
            <!-- <span>{{ time[0] }}</span> -->
          </p>

        </li>
        <li
          class="message"
          v-for="(message, idx) in messages"
          :key="idx"
          :class="message.author"
        >
        <div>
                <img>
        </div>
          <p >
            <span>{{ message.text }}</span>
            <!-- <span>{{ time[0] }}</span> -->
          </p>
        </li>
      </ul>
    </div>



      <!-- <div class="d-flex justify-content-start mb-4">
        <div class="img_cont_msg">
          <img src="chatbot.png" class="rounded-circle user_img_msg">
        </div>
        <div class="msg_cotainer">
          Hi, how are you samim?
          <span class="msg_time">8:40 AM, Today</span>
        </div>
      </div>



      <div class="d-flex justify-content-end mb-4">
        <div class="msg_cotainer_send">
          Hi jassa i am good tnx how about you?
          <span class="msg_time_send">8:55 AM, Today</span>
        </div>
        <div class="img_cont_msg">
      <img src="user.png" class="rounded-circle user_img_msg">
        </div>
      </div> -->


    </div>


     
      
     <!-- -------------------------------------------------------------------------------- -->

    <div class="card-footer">
      <div class="input-group">
        <input type="text" v-model="message" @keyup.enter="sendMessage" name="" class="form-control type_msg" placeholder="Type your message..."/>
        <div class="input-group-append">
          <span class="input-group-text send_btn" @click="sendMessage"><i class="fas fa-location-arrow"></i></span>
        </div>
      </div>
    </div>
  </div>

  


  <!-- ---------------------------------------------------------------------- -->


</template>
<script>
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import '../../App.css';

var data = { soundurl : 'n.mp3'} 

import axios from 'axios'
export default {
  name: 'ChatBot',
  data: () => ({
    elementVisible: false,
    welcome: 'Hello, welcome to the Quiobot chatbot. I can answer questions about Medical problem , What can i help you with ?',
    message: '',
    messages: [],
    time: [1,2],
    data: data,
  }),
  


//   mounted() {
//     var audio = new Audio('n.mp3'); // path to file
//     audio.play();
// },

created() {
            setTimeout(() => this.elementVisible = true, 3000)
        },


mounted:function(){
        this.playSound(); //method1 will execute at pageload
        // this.ShowWelcome ()
        // setTimeout(() => this.playSound() = false, 500);
  },

  // methods:{
  //       callFunction: function () {
  //           var v = this;
  //           setTimeout(function () {
  //               v.inforamtion = "Hi pakainfo Website, SetTimeout is working pakainfo fine.";
  //           }, 3000);
  //       }
  //   },
  //   mounted () {
  //     this.callFunction()
  //   },

  methods: {

    // ShowWelcome (){
    //   this.welcome = 'Hello, welcome to the Quiobot chatbot. I can answer questions about Medical problem , What can i help you with ?';
    //   setTimeout(function () {
    //     console.log('Heey')
    //         }, 3000);
    // },

    
    playSound () {
      var audio = new Audio(data.soundurl);
      setTimeout(function () {
        audio.play()
            }, 3000);
     
    },
    async sendMessage() {
      const message = this.message

      this.messages.push({
        text: message,
        author: 'client'
      })

      this.message = ''


      // await axios
      //       .post(
      //         "http://127.0.0.1:8008/chatbot",{question:message},
      // )
      //       .then((response) => {
      //           // this.messages.push({
      //           // text: response.data.user,
      //           // author: 'server',
      //           console.log(response)
      //       // })
      //       // console.log(response.data.user)
      //         })

      axios.get(`http://34.132.23.12/chatbot?question=${message}`)
      .then(res => {
        this.messages.push({
          text: res.data,
          author: 'server',
        })
        var audio = new Audio(data.soundurl);
      audio.play();

        this.$nextTick(() => {
          this.$refs.chatbox.scrollTop = this.$refs.chatbox.scrollHeight
        })
      })
    }
  }
}
</script>
<style scoped lang="scss">

.chat-box,
.chat-box-list {
  display: flex;
  flex-direction: column;
  list-style-type: none;
}

.chat-box-list-container {
  overflow: scroll;
  margin-bottom: 1px;
}

.chat-box-list {
  padding-left: 10px;
  padding-right: 10px;



  span {
    padding: 8px;
    color: white;
    border-radius: 4px;
  }

  .server {
    span {
      // background: #000;
    }
    p {
      float: left;
    }
    img {
        height: 40px;
        width: 40px;
        // border:1.5px solid #f5f6fa;
        float: left;
        content:url(https://i.postimg.cc/vBVgY5GH/Untitled-design-11.png);
    }
  }

  .client {
    span {
      // background: #000;
    }
    p {
      float: right;
    }
    img {
        height: 40px;
        width: 40px;
        // border:1.5px solid #f5f6fa;
        float: right;
        content:url(https://i.postimg.cc/13W9CmhZ/user.png);
    }
  }
}

.chat-box {
  margin: 10px;
  border: 1px solid #999;
  width: 50vw;
  height: 50vh;
  border-radius: 4px;
  margin-left: auto;
  margin-right: auto;
  align-items: space-between;
  justify-content: space-between;
}

.chat-inputs {
  display: flex;
  
  input {
    line-height: 3;
    width: 100%;
    border: 1px solid #999;
    border-left: none;
    border-bottom: none;
    border-right: none;
    border-bottom-left-radius: 4px;
    padding-left: 15px;
  }

  button {
    width: 145px;
    color: white;
    background: #0070C8;
    border-color: #999;
    border-bottom: none;
    border-right:none;
    border-bottom-right-radius: 3px;
  }
}
</style>