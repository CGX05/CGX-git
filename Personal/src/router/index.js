import { ElMessage } from 'element-plus';
import {createRouter, createWebHistory} from 'vue-router'

const routes=[
    {
        path:'/',
        name:'Home',
        component: () => import('../views/home.vue')
    },
    {
        path:'/login',
        name:'Login',
        component: () => import('../views/Login.vue')

    },
    {
        path:'/lookarticle/:id',
        name:'LookArticle',
        component: () => import('../views/LookArticle.vue')
    },
    {
        path:'/lssuearticle',
        name:'LssueArticle',
        component: () => import('../views/LssueAricle.vue'),
        meta:{requireAuth:true}
    },
    {
        path:'/managearticle',
        name:'ManageArticle',
        component: () => import('../views/ManageAricle.vue'),
        meta:{requireAuth:true}
    },
    {
        path:'/user',
        name:'User',
        component: () => import('../views/User.vue'),
        meta:{requireAuth:true}
    },
    {
        path:'/comment',
        name:'Comment',
        component: () => import('../views/Comment.vue'),
        meta:{requireAuth:true}
    },
    {
        path:'/tag',
        name:'Tag',
        component: () => import('../views/tag.vue'),
        meta:{requireAuth:true}
    },
    {
        path:'/about',
        name:'About',
        component: () => import('../views/about.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

// 全局前置守卫
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token');
    if(to.meta.requireAuth){
        if(token){
            next();
        }else{
            next('/Login');
            ElMessage.error('该页面需要登录授权，请先登录');
        }
    }else{
        next();
    }
})
export default router;
