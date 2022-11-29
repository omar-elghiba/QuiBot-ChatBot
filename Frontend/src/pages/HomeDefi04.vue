<template>
    <div class="home-defi-4">
        <Header6 />
        <Banner8 id="Home"/>
        <FAQ id="RoadMap"/>
        <Parner4 id="Technologies"/>
        
        <!-- <About8 id="About As"/> -->
        <RoadMap8 id="Training"/>
        <FAQ8 id="FAQ"/>
        <Footer5 id="Contact"/>
        <!-- <Footer id="Subscribe"/> -->
        <!-- <Feature7 id="Services"/>
        <Token4 />
        <Allocation5 />
        <Team9 />
        <Blog5 /> -->


    </div>
</template>

<script>
import Header6 from '../components/Header/Header6'
import Banner8 from '../components/Banner/Banner8'
// import About8 from '../components/About/About8'
// import Feature7 from '../components/Feature/Feature7'
import RoadMap8 from '../components/RoadMap/RoadMap8'
// import Allocation5 from '../components/Allocation/Chart5'
// import Team9 from '../components/Team/Team9'
// import Token4 from '../components/Token/Token4'
import Parner4 from '../components/Parner/Parner4'
// import Blog5 from '../components/Blog/Blog5'
import FAQ8 from '../components/FAQ/FAQ8'
import Footer5 from '../components/Footer/Footer5'
// import Footer from '../components/Footer/Footer'
import FAQ from '../components/FAQ/FAQ'


export default {
    name: 'HomeNFT01',
    components: {
        Header6,
        Banner8,
        // About8,
        RoadMap8,
        FAQ,
        // Feature7,
        // Allocation5,
        // Team9,
        // Token4,
        Parner4,
        // Blog5,
        FAQ8,
        Footer5,
        // Footer,
    }
}
</script>