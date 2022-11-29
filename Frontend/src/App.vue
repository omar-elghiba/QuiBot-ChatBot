<template>
    <div>
        <router-view />
        <BackToTop />
    </div>    
</template>

<script>

import BackToTop from './components/Header/BackToTop.vue'

export default {
    name: 'App',
    components: {
        BackToTop,
    },
}
</script>