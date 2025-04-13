<template>
    <div class="person">
        <h2>姓名：{{name}}</h2>
        <h2>年龄：{{age}}</h2>
        <button @click="changename">修改名字</button>
        <button @click="changeage">修改年龄</button>
        <button @click="showtel">点击</button>

    </div>
</template>

<script lang="ts">
    export default{
        name:'Person',
        data(){
            return{
                name:'cgx',
                age:20,
                tel:'110'
            };
        },
        methods:{
            showtel(){
                alert(this.tel)
            },
            changename(){
                this.name='chenguangxaun'
            },
            changeage(){
                this.age+=1
            }
        }
    }
</script>

<style>
    .person{
        background-color: blue;
    }
</style>