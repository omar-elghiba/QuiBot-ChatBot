<template>
    <div class="content-tab" >                   
        <div class="content-inner content-8" v-for="item in dataTeam" :key="item.id">
            <div class="team-box__info" v-for="item in dataTeam" :key="item.id">
                <h6 class="position">{{item.position}}</h6>
                <h5 class="name">{{item.name}}</h5>
                <p class="text fs-14">{{item.text}}</p>
                <ul class="list-social">
                    <li v-for="icon in item.listsocial" :key="icon.id">
                        <router-link :to="icon.link"><span :class="icon.icon"></span></router-link>
                    </li>
                </ul>
            </div>                                                          
        </div>                         
    </div>
</template>

<script>

export default {
    name: 'Faq',
    data (){
        return {
            dataTeam: [
                 {
                    position: "Researcher, token economics",
                    name: "EVOL Roadman",
                    text: "Co-founder of Launch School, previously worked on enterprise data solutions at IBM Silicon Valley Lab, consultant & engineer.",
                    listsocial: [
                        {
                            id: 1,
                            icon: 'icon-LinkedIn',
                            link: '#'
                        },
                        {
                            id: 2,
                            icon: 'icon-facebook',
                            link: '#'
                        },
                        {
                            id: 3,
                            icon: 'icon-Instagram',
                            link: '#'
                        },
                        {
                            id: 4,
                            icon: 'icon-telegram',
                            link: '#'
                        },
                    ]
                },
            ]
        }    
    },
}
</script>