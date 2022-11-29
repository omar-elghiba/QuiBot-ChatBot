<template>
    <div >
        <h2 
            class=" accordion-header"
            :class="{'accordion-active': visible}"
            @click="open"
        >
            <slot name="accordion-trigger"></slot>
        </h2>

        <transition 
            name="accordion"
            @enter="start"
            @after-enter="end"
            @before-leave="start"
            @after-leave="end"
        >
            <div   class="accordion-body"  v-show="visible"    >
                <slot name="accordion-content"></slot>
            </div>
        </transition>
    </div>
</template>

<script>
export default {
    name: 'AccordionItem',
    props: {},
    inject: ["Accordion"],
    data() {
        return {
            index: null
        };
    },
    computed: {
        visible() {
            return this.index == this.Accordion.active;
        }
    },
    methods: {
        open() {
            if (this.visible) {
                this.Accordion.active = null;
            } else {
                this.Accordion.active = this.index;
            }
        },
        start(el) {
            el.style.height = el.scrollHeight + "px";
        },
        end(el) {
            el.style.height = "";
        }
    },
    created() {
        this.index = this.Accordion.count++;
    }
}
</script>