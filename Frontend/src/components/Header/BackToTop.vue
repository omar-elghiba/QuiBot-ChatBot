<template>
    <div id="scroll-top"
        @click="scrollToTop()" 
        :class="[ {'show': isTop}]"
    >
    </div>  
</template>

<script>
export default {
    name: 'BackToTop',
    data (){
        return {
            isTop: false
        }
    },
    methods: {
        scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth',
        })
        },
    },
    mounted(){
        const that = this
        window.addEventListener('scroll', () => {
            let scrollPos = window.scrollY
            if(scrollPos >= 300){
                that.isTop = true
            } else {
                that.isTop = false
            }
        })
    }
}
</script>