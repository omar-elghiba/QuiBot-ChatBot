<template>
    <div class="react-tabs">
        <ul class="menu-tab">
            <li  v-for="tab in dataTab"   :key="tab"  :class="['react-tabs__tab  ', { 'react-tabs__tab--selected': currentTab === tab.currentTab }]"   @click="currentTab = tab.currentTab">
                <h5> {{ tab.title }}</h5>
            </li>
        </ul>
	    <Component :is="currentTab" class="tab" />
    </div>
</template>

<script>

import General from './General.vue'
import Token from './Token.vue'
import RoadMap from './RoadMap.vue'
import Legal from './Legal.vue'

  
export default {
    components: {
        General,
        Token,
        RoadMap,
        Legal,
    },
    data() {
        return {
            currentTab: 'General',
            dataTab: [
                {
                    id: 1,
                    currentTab: 'General',
                    title: "General",
                },
                {
                    id: 2,
                    currentTab: 'Token',
                    title: "Token",
                },
                {
                    id: 3,
                    currentTab: 'Legal',
                    title: "Legal",
                },
                {
                    id: 4,
                    currentTab: 'RoadMap',
                    title: "RoadMap",
                },
                
            ]
        }
    }
}

</script>