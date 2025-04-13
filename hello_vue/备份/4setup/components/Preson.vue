<template>
    <div class="person">
        <h2>姓名：{{name}}</h2>
        <h2>年龄：{{age}}</h2>
        <button @click="changename">修改名字</button>
        <button @click="changeage">修改年龄</button>
        <button @click="showtel">点击</button>

    </div>
</template>

<script lang="ts" setup name="person">
import { ref } from 'vue'   //引入ref
            // 数据
            let name=ref('cgx')   //ref()响应式
            let age=ref(20)
            let tel='13433803373' 

            // 方法
            function changename(){
                name.value='chenguangxuan'  //这样修改不是响应式界面
                console.log(name.value)    //加value响应式
            }
            function changeage(){
                age.value+=1
                console.log(age.value)
            }
            function showtel(){
                alert(tel)
            }
        
</script>


<style>
    .person{
        background-color: blue;
    }
</style>