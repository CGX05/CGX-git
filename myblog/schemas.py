from pydantic import BaseModel
from typing import Optional

# 注册用户
class User(BaseModel):
    id:None
    username:str=None
    password:str=None
    phone:str=None
    email:str=None
    time:str=None
    role:None

# 登陆用户
class Login(BaseModel):
    username:str
    password:str

# 更新用户数据
class users(BaseModel):
    id:Optional[int]=None
    username:str
    password:str
    phone:str
    emali:str
