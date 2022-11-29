<template>
    <div>
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'Accordion',
    props: {},
    data() {
        return {
            Accordion: {
                count: 0,
                active: true
            }
        };
    },
    provide() {
        return { Accordion: this.Accordion };
    }
}
</script>