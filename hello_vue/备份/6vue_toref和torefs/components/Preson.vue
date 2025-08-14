<template>
    <div class="person">
        <h2>扫一辆{{car.brand}}现需要{{car.price}}元</h2>
        <button @click="changeprice">修改价格</button>
        
    </div>
</template>

<script lang="ts" setup name="person">
    import {reactive,toRefs,toRef} from 'vue'

    //数据
    let car=reactive({brand:'共享单车',price:1})
    

    //torefs
    // let{brand,price}=toRefs(car)

    // toRef
    // let brand_a=toRef(car.brand)

    // 方法
    function changeprice(){
        car.brand="自行车"
    }

</script>


<style>
    .perso{
        color: aqua;
    }
</style>