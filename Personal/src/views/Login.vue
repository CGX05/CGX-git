<template>
    <div v-if="islogin" class="welcome-container">
        <h1>欢迎登录，{{ user }}</h1>
        <!-- <button @click="logout">退出登录</button> -->
        <el-button type="danger" @click="logout">退出登录</el-button>
    </div>
    <div class="login-container" v-else>
        <h1>欢迎登录</h1>
        <el-form label-width="80px" :model="UserForm" :rules="LoginRules" ref="loginForm">
            <el-form-item label="用户名" prop="username">
                <el-input v-model="UserForm.username" placeholder="请输入用户名" ></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="UserForm.password" placeholder="请输入密码"></el-input>
            </el-form-item>
            <!-- <el-form-item label="验证码">
                <el-input v-model="captcha" placeholder="请输入验证码"></el-input>
                <img src="captcha_url" alt="验证码" @click="refreshCaptcha" style="cursor: pointer;">
            </el-form-item> -->
            <el-form-item>
                <el-button type="primary" @click="login">登录</el-button>
            </el-form-item>
            <el-form-item>
            <div class="flex justify-between w-full">
                <el-button type="primary" @click="register">注册</el-button>
                <el-button type="info" @click="forget">忘记密码</el-button>
            </div>
            </el-form-item>
        </el-form>
    </div>
</template>

<script setup>
import { ElMessage, ElMessageBox } from 'element-plus';
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
// 使用路由
const router = useRouter();
// 定义表单变量
const UserForm = reactive({
    username: '',
    password: ''
});
// 定义表单规则
const LoginRules=({
    username: [
        { required: true, message: '请输入用户名', trigger: 'red' },
        { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'red' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'red' },
        { min: 5, max: 10, message: '长度在 6 到 10 个字符', trigger:'red'}
    ]
})
// 校验是否符合规则
const loginForm = ref(null);
const login=()=>{
    loginForm.value.validate((valid)=>{
        if(valid){
            axios.post("http://8.134.127.43:8000/token", UserForm).then((response)=>{
                const data=response.data;
                if(data.success){
                    ElMessage.success("登录成功")
                    localStorage.setItem("token", data.token);
                    localStorage.setItem("user", data.user);
                    router.push("/");
                    // console.log(data);
                }else{
                    ElMessage.error(data.message||"登录失败")
                }
            }).catch((error)=>{
                console.error(error);
                ElMessage.error('登录失败，请稍后再试');
            })
        }
    })
}
// 登陆成功表单变化
onMounted(() => {
    welcome_login();
});
const islogin = ref(false);
const user=ref();
const welcome_login = () => {
      const token = localStorage.getItem('token');
      if (token) {
        islogin.value = true;
        user.value = localStorage.getItem('user');
      }
    };
// 退出登录
const logout = () => {
    localStorage.removeItem('token');
    islogin.value = false;
    ElMessage.success('退出登录成功');
    router.push('/Login');
};
const register=()=>{
    ElMessage.error("注册功能尚未实现,有需要请联系管理员")
}
const forget=()=>{
    ElMessage.error("忘记密码功能尚未实现,有需要请联系管理员")
}

</script>

<style>
.login-container {
    max-width: 650px;
    margin: 0 auto;
    padding: 88px;
    border: 1px solid #ece2e2;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(199, 194, 194, 0.1);
}
.login-container h1 {
    text-align: center;
    margin-bottom: 26px;
}
.login-container .el-form-item {
    margin-bottom: 15px;
}
.login-container .el-button {
    width: 100%;
}
.flex {
  display: flex;
}

.justify-between {
  justify-content: space-between;
}

.w-full {
  width: 100%;
}
.welcome-container {
  display: flex;
  flex-direction: column; 
  justify-content: center;     
  align-items: center;   
  height: 100vh;
  text-align: center;        
  gap: 20px;           
  color: #333;
}

.welcome-container h1 {
  margin: 0;
  font-size: 1.8rem;
}

.welcome-container .el-button {
  padding: 12px 24px;
  font-size: 16px;
}
</style>