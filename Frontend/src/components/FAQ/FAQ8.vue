<template>
    <section class="section-faq style-2" id="faq">
        <div class="container">
            <div class="row">
                <div class="col-xl-5 col-md-12">
                    <div class="faq__images">
                        <img src='~@/assets/images/layout/faq-h8.f6f0bae0.png' alt="Image" />
                    </div>
                </div>
                <div class="col-xl-7 col-md-12">
                    <div class="faq__content">
                        <div class="block-text">
                            <h3 class="heading">{{title}}</h3>
                            <p class="fs-17">{{desc}}</p>
                        </div>
    
                        <div class="flat-tabs">
                                <Tab />
                            </div>
                    </div>
                </div>
                
            </div>
        </div>
    </section>
</template>

<script>

import Tab from "../Tab/Tab7/Tab";
import "./styles.scss";


export default {
    name: 'Faq',
    data (){
        return {
            title: 'Frequently asked questions ',
            desc : 'Below we’ve provided a bit of ICO, ICO Token, cryptocurrencies, and few others.',
        }    
    },
    components: {
        Tab,
    }
}
</script>