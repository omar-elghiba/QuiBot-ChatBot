<template>
    <div class="content-tab">
        <accordion class="content-inner flat-accordion"> 
            <accordion-item class="accordion-item" v-for="item in dataFaq.slice(22,26)" :key="item.id">
                <template v-slot:accordion-trigger class="accordion-header" :class="{'accordion__trigger_active': item.show}">
                    <button class="accordion-button">
                        {{item.title}}
                    </button>
                </template>
                <template v-slot:accordion-content>
                    <p class="toggle-content">{{item.content}}</p>
                </template>
            </accordion-item>
            

        </accordion>
    </div>
</template>

<script>
import Accordion from "../../Accordion/Accordion";
import AccordionItem from "../../Accordion/AccordionItem";
import { dataFaq } from '../../../fake-data/data-faq';


export default {
    name: 'Faq',
    data (){
        return {
            dataFaq,
        }    
    },
    components: {
        Accordion,
        AccordionItem,
    }
}
</script>