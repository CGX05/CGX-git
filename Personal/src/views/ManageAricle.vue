<template>
        <div class="user-table">
        <h1 class="title">用户管理</h1>
        <el-table :data="aricledata" border stripe size="default" style="width: 100%;height: 100%" max-height="100%">
        <el-table-column prop="id" label="ID" />
        <el-table-column prop="title" label="标题" />
        <el-table-column prop="time" label="发布时间" />
        <el-table-column prop="user" label="用户" />
        <el-table-column prop="uptime" label="修改时间" />
        <el-table-column label="操作">
            <template #default="scope">
                <el-button type="primary" @click="() => handleEdit(scope.row)">编辑</el-button>
                <el-button type="danger" @click="() => handleDelete(scope.row)">删除</el-button>
            </template>
        </el-table-column>
    </el-table>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import request from '../utils/request'
const aricledata=ref([])
onMounted(()=>{
    getAricle()
})
const getAricle=async()=>{
    try{
        const response = await request.get('/api/article/list')
        aricledata.value = response.data
    }catch(error){
        console.error('获取文章列表失败:', error)
    }
}
</script>
