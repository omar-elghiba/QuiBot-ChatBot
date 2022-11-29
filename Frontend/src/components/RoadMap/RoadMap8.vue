
<template>
    <section class="road-map style-8" id="roadmap">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="block-text center">
                        <h2 class="heading">{{title}}</h2>
                        <p class="fs-17">{{desc}}</p>
                    </div>

                    <div class="road-map__main">
                       <carousel class="swiper-roadmap-7"
                            :settings='settings' 
                            :breakpoints='breakpoints'
                        >
                            <Slide v-for="slide in dataRoadMap.slice(21,26)" :key="slide.id">
                                <div class="box-roadmap" :class="slide.classAction" data-aos="fade-up" data-aos-duration="1000">
                                    <!-- <p class="time">{{slide.time}}</p> -->
                                    <h5 class="title">{{slide.title}}</h5>
                                    <!-- <ul class="list">
                                        <li v-for="text in slide.list" :key="text.id">
                                            <div class="dot"></div>
                                            <p class='fs-17'>{{text.text}}</p>
                                        </li>
                                    </ul> -->
                                </div>
                                
                            </Slide>
                            <template #addons>
                                <pagination />
                            </template>
                        </carousel>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import "./styles.scss";

import { defineComponent } from 'vue';
import { Carousel, Slide, Pagination,  } from 'vue3-carousel';

import 'vue3-carousel/dist/carousel.css';
import { dataRoadMap } from '../../fake-data/data-roadmap';


export default defineComponent ({
   name: "About3",
    components: {
        Carousel,
        Slide,
        Pagination,
    },
    data: () => ({
        dataRoadMap,
        desc: '',
        title: 'QuiBot Chatbot Road Map',
        settings: {
            itemsToShow: 1,
            snapAlign: 'center',
        },
        breakpoints: {
            0: {
                itemsToShow: 1,
                snapAlign: 'center',
			},
            768: {
                itemsToShow: 2,
                snapAlign: 'center',
            },
            1024: {
                itemsToShow: 4,
                snapAlign: 'center',
            },
            1200: {
                itemsToShow: 4,
                snapAlign: 'center',
            },
        },
    }),
})

</script>