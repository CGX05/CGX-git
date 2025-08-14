<template>
  <div class="article-detail">
    <el-card v-if="article" shadow="never">
      <h1>{{ article.title }}</h1>
      <p class="author-time">
        <span>作者：{{ article.user }}</span>
        <span>时间：{{ article.time }}</span>
      </p>
      <div class="content">{{ article.content }}</div>
      <!-- 评论区 -->
      <!-- <div class="comments">
        <h3>评论区</h3>
        <el-card v-for="comment in comments" :key="comment.id" shadow="hover">
          <p><strong>{{ comment.user }}:</strong> {{ comment.content }}</p>
          <span>{{ comment.time }}</span>
        </el-card>
        <div v-if="comments.length === 0" class="loading">暂无评论</div>
        <el-form ref="commentForm" label-width="80px">
          <el-form-item label="评论：">
            <el-input v-model="commentForm.content" placeholder="请输入评论内容"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitComment">提交</el-button>
          </el-form-item>
        </el-form>
      </div> -->

    </el-card>
    <div v-else class="loading">点击主页浏览文章标题点击。。。</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import request from '../utils/request' // 确保导入了请求工具

// 定义响应式变量
const article = ref(null)
const route = useRoute() // 获取路由参数
const comments = ref([])
// 在组件挂载后发送请求
onMounted(async () => {
  try {
    // 从路由参数中获取文章ID
    const { id } = route.params
    console.log('请求文章ID:', id) // 检查是否有正确的ID
    
    // 发送请求到后端（确保路径与后端一致）
    const response = await request.get(`/api/article/data/${id}`)
    article.value = response.data // 赋值给响应式变量
  } catch (error) {
    console.error('请求失败:', error)
  }
})
</script>

<style>
article-detail {
  padding: 20px;
}

.el-card {
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  margin-bottom: 10px;
}

.author-time {
  display: flex;
  justify-content: space-between;
  color: #606266;
  margin-bottom: 20px;
}

.author-time span {
  font-size: 14px;
}

.content {
  line-height: 1.6;
  color: #303133;
}

.loading {
  text-align: center;
  font-size: 18px;
  color: #909399;
}

</style>