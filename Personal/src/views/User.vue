<template>
    <div class="user-table">
        <h1 class="title">用户管理</h1>
        <el-table :data="user" border stripe size="default" style="width: 100%;height: 100%" max-height="100%">
        <el-table-column prop="id" label="ID" />
        <el-table-column prop="username" label="用户" />
        <el-table-column prop="password" label="密码" />
        <el-table-column prop="phone" label="联系方式" />
        <el-table-column prop="emali" label="EMAIL" />
        <el-table-column prop="time" label="TIME" />
        <el-table-column label="操作">
            <template #default="scope">
                <el-button type="primary" @click="() => handleEdit(scope.row)">编辑</el-button>
                <el-button type="danger" @click="() => handleDelete(scope.row)">删除</el-button>
            </template>
        </el-table-column>
    </el-table>
    </div>
    <el-dialog
        v-model="centerDialogVisible"
        title="操作用户"
        width="500"
        align-center>
        <el-form :model="upuser" label-width="120px">
                <el-form-item label="用户">
                <el-input v-model="upuser.username"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                <el-input v-model="upuser.password"></el-input>
                </el-form-item>
                <el-form-item label="联系方式">
                <el-input v-model="upuser.phone"></el-input>
                </el-form-item>
                <el-form-item label="邮箱">
                <el-input v-model="upuser.emali"></el-input>
                </el-form-item>
            </el-form>
        <template #footer>
        <div class="dialog-footer">
            <el-button @click="centerDialogVisible = false">取消</el-button>
            <el-button type="primary" @click="handleUpdate">确定</el-button>
        </div>
        </template>
    </el-dialog>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import request from '../utils/request'
const centerDialogVisible = ref(false)
const router = useRouter()
onMounted(async () => {
    // 获取用户列表
    await getuser();
});
let user=ref([])
const getuser=async()=>{
    try{
        await request.get("/api/v1/users").then((response)=>{
            user.value=response.data
            // console.log(response.data);
        })
    }catch(error){
        ElMessageBox.confirm('获取用户信息失败，请刷新页面或重新登陆。', '错误', {
            confirmButtonText: '确定',
            type: 'error'
        });
        localStorage.removeItem("token");
        router.push("/login");
    }
}
const upuser=ref({})
function handleEdit(row){
    centerDialogVisible.value = true;
    upuser.value = { ...row }; // 深拷贝，避免直接修改原数据
    delete upuser.value.time;
}
function handleUpdate(){ 
    centerDialogVisible.value = false;
        try{
        request.post("api/v1/up_user",upuser.value).then((response)=>{
            if(response.data.success){
                ElMessage.success("修改成功")
                getuser()
            }else{
                ElMessage.error(response.data.message||"修改失败")
                localStorage.removeItem("token");
                router.push("/login");
            }
        })
    }catch(error){
        ElMessage.error("修改失败")
    }
}
function handleDelete(row){
    ElMessageBox.confirm(`确定删除用户 ${row.username} 吗？`, '警告', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
    }).then(()=>{
        try{
            request.delete("api/v1/del_user", { params: { user_id: row.id } }).then((response)=>{
                if(response.data.success){
                    ElMessage.success("删除成功")
                    getuser()
                }else{
                    ElMessage.error(response.data.message||"删除失败")
                    localStorage.removeItem("token");
                    router.push("/login");
                }
            })
        }catch(error){
            ElMessage.error("删除失败")
        }
    })

}
</script>

<style>
.title {
  color: #1e76be;
  margin-bottom: 20px;
}
</style>