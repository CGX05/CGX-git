<template>
    <div class="app">
        <h1>hello</h1>
        <Preson/>
    </div>

</template>


<script lang="ts">
    import Preson from './components/Preson.vue';

    export default{
        name:'App',
        components:{Preson}
    }

</script>


<style>
    .app{
        background-color: aquamarine;
    }

</style>