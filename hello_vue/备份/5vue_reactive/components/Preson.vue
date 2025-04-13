<template>
    <div class="person">
        <h2>扫一辆{{car.brand}}现需要{{car.price}}元</h2>
        <button @click="changeprice">修改价格</button>
        <br>
        <h2>游戏列表：</h2>
        <ul>
            <li v-for="g in games" :key="g.id">{{ g.name }}</li>
        </ul>
        <button @click="changefirst">修改</button>
    </div>
</template>

<script lang="ts" setup name="person">
    import {reactive} from 'vue'

    //数据
    let car=reactive({brand:'共享单车',price:1})
    let games=reactive([{id:'01',name:'CF'},
    {id:'02',name:'cs'},
    {id:'03',name:'ww'},
    ])

    // 方法
    function changeprice(){
        car.price+=1
    }
    function changefirst(){
        games[0].name='球球大作战'
    }

</script>


<style>
    .perso{
        color: aqua;
    }
</style>