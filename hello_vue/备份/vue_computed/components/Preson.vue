<template>
    <div class="person">
        姓：<input type="text" v-model="firstname"> <br>
        名：<input type="text" v-model="lastname"> <br>
        全名：<span>{{ name_a }}</span>
        <button @click="changefullname">修改</button>
    </div>
</template>

<script lang="ts" setup name="person">
    import {reactive,toRefs,toRef, ref,computed} from 'vue'
    
    let firstname=ref('chen')
    let lastname=ref('guangxuan')
    // 定义一个属性可读可写
    let name_a= computed({
        get(){
            return firstname.value.slice(0,1).toUpperCase()+firstname.value.slice(1)+'-'+lastname.value
        },
        set(val){
            const [str1,str2]=val.split('-')
            firstname.value=str1
            lastname.value=str2
        }
    })

    function changefullname(){
        name_a.value='c-gx'
        
    }

</script>


<style>
    .perso{
        color: aqua;
    }
</style>