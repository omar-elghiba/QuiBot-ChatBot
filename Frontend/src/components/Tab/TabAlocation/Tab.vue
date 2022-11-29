<template>
    <div class="react-tabs">
        <ul class="menu-tab">
            <li  v-for="tab in dataTab"   :key="tab"  :class="['react-tabs__tab  ', { 'react-tabs__tab--selected': currentTab === tab.currentTab }]"   @click="currentTab = tab.currentTab" >
                <h6>{{tab.title}}</h6>
            </li>
        </ul>
	    <Component :is="currentTab" class="tab" />
    </div>
</template>

<script>

import Alocation1 from './Allocation1.vue'
import Alocation2 from './Allocation2.vue'

export default {
    components: {
        Alocation1,
        Alocation2,
    },
    data() {
        return {
            currentTab: 'Alocation1',
            dataTab: [
                {
                    id: 1,
                    currentTab: 'Alocation1',
                    title: "Distribution",
                },
                {
                    id: 2,
                    currentTab: 'Alocation2',
                    title: "Funding Allocation",
                },
            ]
        }
    }
}

</script>