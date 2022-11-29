<template>
    <section class="section-partner style-4 " id="partner">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="partner__main">
                        <div class="block-text center">
                            <h3 class="heading">{{title}}</h3>
                            <p class="fs-17">{{desc}}
                            </p>
                        </div>
                        <div class="partner-content">
                        <carousel  class="swiper swiper-partner"
                            :settings='settings' 
                            :breakpoints='breakpoints'
                        >
                            <Slide v-for="slide in dataParter.slice(6,13)" :key="slide.id">
                                <div class="image"><img :src="slide.img" alt="image"></div>                                
                            </Slide>

                        </carousel>
                        <carousel class="swiper swiper-partner"
                            :settings='settings' 
                            :breakpoints='breakpoints'
                        >
                            <Slide v-for="slide in dataParter.slice(12,21)" :key="slide.id">
                                <div class="image"><img :src="slide.img" alt="image"></div>                                
                            </Slide>

                        </carousel>
                        <carousel class="swiper swiper-partner"
                            :settings='settings' 
                            :breakpoints='breakpoints'
                        >
                            <Slide v-for="slide in dataParter.slice(18,27)" :key="slide.id">
                                <div class="image"><img :src="slide.img" alt="image"></div>                                
                            </Slide>

                        </carousel>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { defineComponent } from 'vue';
import { Carousel, Slide  } from 'vue3-carousel';
import "./styles.scss";
import { dataParter } from '../../fake-data/data-partner';

import 'vue3-carousel/dist/carousel.css';

export default defineComponent ({
    name: 'Parner',
    components: {
        Carousel,
        Slide,
    },
    data: () => ({
        dataParter,
        title: 'Technologies',
        desc : '',
        settings: {
            itemsToShow: 1,
            snapAlign: 'center',
        },
        breakpoints: {
            400: {
                itemsToShow: 2,
                snapAlign: 'center',
			},
            768: {
                itemsToShow: 3,
                snapAlign: 'center',
            },
            1024: {
                itemsToShow: 4,
                snapAlign: 'center',
            },
            1200: {
                itemsToShow: 6,
                snapAlign: 'center',
            },
        },
    }),
})
</script>