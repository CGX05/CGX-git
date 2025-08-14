<template>
  <el-carousel :interval="5000" type="card" height="350px">
    <el-carousel-item v-for="item in imgdata" :key="item.id">
        <img :src="item.src" style="width: 100%; height: 100%; object-fit: cover;">
    </el-carousel-item>
  </el-carousel>
  <div>
    <h2>最近文章</h2>
    <div>
      <el-card shadow="never" v-for="article in ardata" :key="article.id">
        <h3><router-link :to="{ name: 'LookArticle', params: { id: article.id } }" class="nav-link">{{ article.title }}</router-link></h3>
        <p>作者：{{ article.user }}</p>
        <span>时间：{{ article.time }}</span>
      </el-card>
    </div>
  </div>
</template>

<script setup>
import { ref,onMounted} from 'vue';
import { ElCarousel, ElCarouselItem, ElCard } from 'element-plus';
import request from '../utils/request'
const imgdata=[
    {id:1,src:new URL('../assets/images/5.jpg', import.meta.url).href},
    {id:2,src:new URL('../assets/images/1.jpg', import.meta.url).href},
    {id:3,src:new URL('../assets/images/2.jpg', import.meta.url).href},
    {id:4,src:new URL('../assets/images/4.png', import.meta.url).href},
]

const ardata=ref([]);
request.get('/api/article/list').then((res)=>{
    // console.log(res.data)
    ardata.value=res.data
})
</script>


<style scoped>

</style>