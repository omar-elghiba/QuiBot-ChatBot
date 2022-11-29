<template>
    <div class="react-tabs">
        <ul class="menu-tab">
            <li  v-for="tab in dataTab"   :key="tab"  :class="['react-tabs__tab  ', { 'react-tabs__tab--selected': currentTab === tab.currentTab }]"   @click="currentTab = tab.currentTab" >
                <div class="image">
                    <img :src="tab.img" alt="ICOLand">
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


import img6 from '../../../assets/images/avt/team-01.jpg'
import img7 from '../../../assets/images/avt/team-02.jpg'
import img8 from '../../../assets/images/avt/team-03.jpg'
import img9 from '../../../assets/images/avt/team-04.jpg'
import img10 from '../../../assets/images/avt/team-05.jpg'
  
export default {
    components: {
        Team1,
        Team2,
        Team3,
        Team4,
        Team5,
    },
    data() {
        return {
            currentTab: 'Team1',
            dataTab: [
                {
                    id: 1,
                    currentTab: 'Team1',
                    img: img6,
                },
                {
                    id: 2,
                    currentTab: 'Team2',
                    img: img7,
                },
                {
                    id: 3,
                    currentTab: 'Team3',
                    img: img8,
                },
                {
                    id: 4,
                    currentTab: 'Team4',
                    img: img9,
                },
                {
                    id: 5,
                    currentTab: 'Team5',
                    img: img10,
                },
            ]
        }
    }
}

</script>