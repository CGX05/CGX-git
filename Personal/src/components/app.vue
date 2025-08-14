<template>
  <div class="common-layout">
    <el-container class="layout-container">
      <!-- 头部 -->
      <el-header class="header-container">
        <div class="header-title">
          <h1>欢迎来到我的网站</h1>
        </div>
        <div class="nav">
          <nav>
            <ul>
              <li><router-link to="/" class="nav-link">主页</router-link></li>
              <li><router-link to="/lookarticle" class="nav-link">文章浏览</router-link></li>
              <li><router-link to="/lssuearticle" class="nav-link">文章发布</router-link></li>
              <li><router-link to="/managearticle" class="nav-link">文章管理</router-link></li>
              <li><router-link to="/user" class="nav-link">用户管理</router-link></li>
              <li><router-link to="/comment" class="nav-link">评论管理</router-link></li>
              <li><router-link to="/tag" class="nav-link">标签管理</router-link></li>
              <li><router-link to="/about" class="nav-link">关于我们</router-link></li>
              <li><router-link to="/login" class="nav-link">登录</router-link></li>
            </ul>
          </nav>
        </div>
      </el-header>

      <!-- 主体 -->
      <el-main class="main-content">
        <!-- <router-view></router-view> -->
      </el-main>

      <!-- 底部 -->
      <el-footer class="footer-container">
        <div class="footer-text">
          <p>© 2025 我的个人网站. 保留所有权利.</p>
          <p>联系方式:2717630445@qq.com</p>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<style scoped>
/* 基础重置与全屏适配 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.common-layout {
  width: 100%;
  height: 100vh;
  overflow: hidden;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.layout-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header-container {
  background: linear-gradient(135deg, #1e5a81, #2a5298);
  color: rgb(248, 251, 253);
  padding: 15px 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  text-align: center;
}

.header-title h1 {
  margin: 0;
  font-size: 1.6rem;
  font-weight: 600;
  letter-spacing: 0.8px;
}

.nav ul {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
  padding: 0;
  margin: 0;
}

.nav-link {
  color: #ffffffcc;
  text-decoration: none;
  font-size: 1rem;
  padding: 8px 14px;
  border-radius: 8px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover,
.nav-link.router-link-exact-active {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.2);
}

/* 活跃路由下划线动画 */
.nav-link.router-link-exact-active::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 3px;
  background-color: #00d4ff;
  border-radius: 2px;
  animation: growLine 0.3s ease-out forwards;
}

@keyframes growLine {
  from {
    width: 0;
  }
  to {
    width: 60%;
  }
}

/* 主体内容区域 */
.main-content {
  flex: 1;
  padding: 20px;
  background-color: #f9fafa;
  overflow-y: auto;
}

/* 底部样式 */
.footer-container {
  background: #f0f2f5;
  color: #666;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 0.9rem;
  border-top: 1px solid #eaeaea;
}

.footer-text {
  text-align: center;
}

/* 响应式设计 */
@media (min-width: 769px) {
  .header-container {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  .header-title h1 {
    font-size: 1.8rem;
    margin-right: auto;
  }

  .nav ul {
    gap: 20px;
    flex-wrap: nowrap;
  }

  .nav-link {
    font-size: 1.05rem;
    padding: 10px 16px;
  }
}

@media (max-width: 480px) {
  .header-container {
    padding: 12px;
  }

  .header-title h1 {
    font-size: 1.4rem;
  }

  .nav ul {
    gap: 10px;
  }

  .nav-link {
    font-size: 0.9rem;
    padding: 6px 10px;
  }

  .footer-text {
    font-size: 0.85rem;
  }
}
</style>