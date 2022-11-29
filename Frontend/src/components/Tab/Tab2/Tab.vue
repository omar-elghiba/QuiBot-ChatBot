<template>
    <div class="react-tabs">
        <ul class="menu-tab">
            <li  v-for="tab in dataTab"   :key="tab"  :class="['react-tabs__tab  ', { 'react-tabs__tab--selected': currentTab === tab.currentTab }]"   @click="currentTab = tab.currentTab">
                <h6> {{ tab.title }}</h6>
            </li>
        </ul>
	    <Component :is="currentTab" class="tab" />
    </div>
</template>

<script>

import General from './General.vue'
import Pre_ICO_ICO from './Pre.vue'
import Token from './Token.vue'
import Client from './Client.vue'
import Legal from './Legal.vue'

  
export default {
    components: {
        General,
        Pre_ICO_ICO,
        Token,
        Client,
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
                    currentTab: 'Pre_ICO_ICO',
                    title: "Pre ICO & ICO",
                },
                {
                    id: 3,
                    currentTab: 'Token',
                    title: "Token",
                },
                {
                    id: 4,
                    currentTab: 'Client',
                    title: "Client",
                },
                {
                    id: 5,
                    currentTab: 'Legal',
                    title: "Legal",
                },
            ]
        }
    }
}

</script>