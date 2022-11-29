
<template>
    <section class="page-404">
            <div class="container">
                <div class="row">
                    <div class="main-404">
                        <img src='~@/assets/images/layout/404.png' alt="ICOLand" />
                        <h2 class="title">{{title}}</h2>
                        <p>{{desc}}</p>
                        <a class="btn-action style-1" href="/"><span class="effect">Back To Homepage</span></a>
                    </div>
                </div>
            </div>
        </section>
</template>

<script>

export default {
    name: "Feature",
     data (){
        return {
            title : 'Page not found',
            desc : 'Duis dolor sit amet, consectetur adipiscing elitvestibulum in pharetra.',
        }    
    }
};
</script>
            
            