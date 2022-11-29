<template>
    <div class="content-tab" >                   
        <div class="content-inner">
            <div class="list-progress">
                <div class="progressbar">
                    <div class="title">
                        <p>Marketing: 25%</p>
                    </div>
                    <div class="barline">
                        <div class="countbar s1">
                            <div class="progress-bar" style="width: 25%;"></div>
                        </div>
                    </div>
                </div>
                <div class="progressbar">
                    <div class="title">
                        <p>Bussiness Development: 25%</p>
                    </div>
                    <div class="barline">
                        <div class="countbar s2">
                            <div class="progress-bar" style="width: 25%;"></div>
                        </div>
                    </div>
                </div>
                <div class="progressbar">
                    <div class="title">
                        <p>Product Development: 10%</p>
                    </div>
                    <div class="barline">
                        <div class="countbar s3">
                            <div class="progress-bar" style="width: 10%;"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="chart-bar">
                <PieChart v-bind:chartData="this.state.chartData" v-bind:chartOptions="this.state.chartOptions" :width="240" :height="240" />
            </div>
            <div class="list-progress right">
                <div class="progressbar">
                    <div class="title">
                        <p>Reserve: 10%</p>
                    </div>
                    <div class="barline">
                        <div class="countbar s4">
                            <div class="progress-bar" style="width: 10%;"></div>
                        </div>
                    </div>
                </div>
                <div class="progressbar">
                    <div class="title">
                    <p>Reserve: 10%</p>
                    </div>
                    <div class="barline">
                        <div class="countbar s5">
                            <div class="progress-bar" style="width: 10%;"></div>
                        </div>
                    </div>
                </div>
                <div class="progressbar">
                    <div class="title">
                        <p>Token Sale: 20%</p>
                    </div>
                    <div class="barline">
                        <div class="countbar s6">
                            <div class="progress-bar" style="width: 20%;"></div>
                        </div>
                    </div>
                </div>
            </div>                                               
        </div>                         
    </div>
</template>

<script>

import PieChart from '../../Allocation/PieChart/PieChart.vue';
import { defineComponent } from 'vue'
export default defineComponent ({
  name: "Chart",
  components: {
        PieChart,
    },
  data (){
        return {
            state: {
                chartData: {
                datasets: [
                    {
                    data: [25, 25, 10, 10,10, 20],
                    backgroundColor: ['#3d88fb', '#5637c8', '#00d199', '#c87b07', '#a92535', '#9116cd']
                    }
                ],
                labels: [
                    'Marketing',
                    'Bussiness Development',
                    'Product Development',
                    'Reserve',
                    'Reserve',
                    'Token Sale'
                    
                ],
                },
                chartOptions: {
                    responsive: false,
                    legend: {
                    display: false
                    }
                },
            }
        }    
    },
});
</script>
