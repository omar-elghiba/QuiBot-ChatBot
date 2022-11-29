<template>
    <div class="content-tab" >                   
        <div class="content-inner" v-for="item in dataTeam" :key="item.id">
            <div class="image">
                <img :src="item.img" alt="ICOLand" />
            </div>
            <div class="content">
                <div class="block-text">
                    <h3 class="heading">{{item.title}}</h3>
                    <p key={item}>{{item.desc}}</p>
                </div>
                <div class="info">
                        <span class="icon-union-01"></span>
                        <span class="icon-union-02"></span>
                        <span class="icon-union-03"></span>
                        <span class="icon-union-04"></span>
                    <h4 class="name">{{item.name}}</h4>
                    <p class="position">{{item.position}}</p>
                    <p class="text">{{item.text}}</p>
                    <div class="list-social">
                        <li  v-for="icon in item.listsocial" :key="icon.id">
                            <route-link :to="icon.link" ><span :class="icon.icon"></span> </route-link>
                        </li>
                    </div>
                </div>
            </div>                                                         
        </div>                         
    </div>
</template>

<script>

import img from '../../../assets/images/avt/team-v03.png'



export default {
    name: 'Faq',
    data (){
        return {
            dataTeam: [
                 {
                    img: img,
                    title: "Executive Team",
                    desc: "Our team player alway finds effective ways to improve the product and process",
                    name: "Charlee Mangar",
                    position: "Co-founder & COO",
                    text: 'As Sneakerheadz is a members only club, holding one of our Genesis "OG" NFTs grants you access to exclusivity only we can provide.',
                    listsocial: [
                        {
                            id: 1,
                            icon: 'icon-twitter',
                            link: '#'
                        },
                        {
                            id: 2,
                            icon: 'icon-facebook',
                            link: '#'
                        },
                        {
                            id: 3,
                            icon: 'icon-place',
                            link: '#'
                        },
                        {
                            id: 4,
                            icon: 'icon-reddit',
                            link: '#'
                        },
                    ]
                },
            ]
        }    
    },
}
</script>