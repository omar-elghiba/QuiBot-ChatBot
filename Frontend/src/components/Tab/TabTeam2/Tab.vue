<template>
    <div class="react-tabs">
        <ul class="menu-tab">
            <li  v-for="tab in dataTab"   :key="tab"  :class="['react-tabs__tab  ', { 'react-tabs__tab--selected': currentTab === tab.currentTab }]"   @click="currentTab = tab.currentTab" >
                <div class="team-box__image">
                    <img :src="tab.img" alt="ICOLand" />
                </div>
            </li>
        </ul>
	    <Component :is="currentTab" class="tab" />
    </div>
</template>

<script>

import Team1 from './Team1.vue'
import Team2 from './Team2.vue'
import Team3 from './Team3.vue'
import Team4 from './Team4.vue'
import Team5 from './Team5.vue'
import Team6 from './Team6.vue'
import Team7 from './Team7.vue'
import Team8 from './Team8.vue'
import Team9 from './Team9.vue'
import Team10 from './Team10.vue'
import Team11 from './Team11.vue'
import Team12 from './Team12.vue'




import img1 from '../../../assets/images/avt/team-map-01.png'
import img2 from '../../../assets/images/avt/team-map-02.png'
import img3 from '../../../assets/images/avt/team-map-03.png'
import img4 from '../../../assets/images/avt/team-map-04.png'
import img5 from '../../../assets/images/avt/team-map-05.png'
import img6 from '../../../assets/images/avt/team-map-06.png'
import img7 from '../../../assets/images/avt/team-map-07.png'
import img8 from '../../../assets/images/avt/team-map-08.png'
import img9 from '../../../assets/images/avt/team-map-09.png'
import img10 from '../../../assets/images/avt/team-map-10.png'
import img11 from '../../../assets/images/avt/team-map-11.png'
import img12 from '../../../assets/images/avt/team-map-12.png'

  
export default {
    components: {
        Team1,
        Team2,
        Team3,
        Team4,
        Team5,
        Team6,
        Team7,
        Team8,
        Team9,
        Team10,
        Team11,
        Team12,
    },
    data() {
        return {
            currentTab: 'Team1',
            dataTab: [
                {
                    id: 1,
                    currentTab: 'Team1',
                    img: img1,
                },
                {
                    id: 2,
                    currentTab: 'Team2',
                    img: img2,
                },
                {
                    id: 3,
                    currentTab: 'Team3',
                    img: img3,
                },
                {
                    id: 4,
                    currentTab: 'Team4',
                    img: img4,
                },
                {
                    id: 5,
                    currentTab: 'Team5',
                    img: img5,
                },
                {
                    id: 6,
                    currentTab: 'Team6',
                    img: img6,
                },
                {
                    id: 7,
                    currentTab: 'Team7',
                    img: img7,
                },
                {
                    id: 8,
                    currentTab: 'Team8',
                    img: img8,
                },
                {
                    id: 9,
                    currentTab: 'Team9',
                    img: img9,
                },
                {
                    id: 10,
                    currentTab: 'Team10',
                    img: img10,
                },
                {
                    id: 11,
                    currentTab: 'Team11',
                    img: img11,
                },
                {
                    id:2,
                    currentTab: 'Team12',
                    img: img12,
                },
            ]
        }
    }
}

</script>