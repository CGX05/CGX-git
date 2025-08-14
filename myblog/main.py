import datetime
import time
import uvicorn
from fastapi import FastAPI,HTTPException,status,Depends
from fastapi.middleware.cors import CORSMiddleware
from db import sql_db
import secrets
import jwt
import schemas
from fastapi.responses import JSONResponse

# 导入子路由
from user import router as users_router
from articlelist import router as article_router
from comment import router as comment_data

app=FastAPI()
app.include_router(users_router,prefix="/api/v1")
app.include_router(article_router,prefix="/api/article")
app.include_router(comment_data,prefix="/api/comments")
# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello():
    return {'message':"hello11!!"}

# 登录验证
secret_key = 'pmiqgtNFFVagSB7DZPPoir7Hb7g25qH1eSiou5fqP5s'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES =60*60*24*30
print(secret_key)
@app.post('/token',summary="登录获取token")
async def token(form:schemas.Login):
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select username,password from user where username=%s and password=%s;"
            cursor.execute(sql,(form.username,form.password))
            user=cursor.fetchone()
            if not user:
                return JSONResponse(content={"success":False,"message":"用户名或密码错误"},status_code=401)
            if form.password != user['password']:
                return JSONResponse(content={"success":False,"message":"用户名或密码错误"},status_code=401)
            payload={"user":user['username'],"exp":int(time.time())+ACCESS_TOKEN_EXPIRE_MINUTES}
            token=jwt.encode(payload,secret_key,algorithm=ALGORITHM)
            return JSONResponse(content={"success":True,"token":token,'user':user['username']})
    except Exception as e:
        print(f"错误{e}")
        return JSONResponse(
            content={"success": False, "message": "系统错误"},
            status_code=500
        )

# 注册用户
@app.post("/into_user")
def into_user(into:schemas.User):
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select username from user where username=%s;"
            cursor.execute(sql,(into.username,))
            user=cursor.fetchall()
            if user:
                return JSONResponse(content={"success": False, "message": "用户存在"}, status_code=400)
            else:
                sql="insert into user values (%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(sql,(into.id,into.username,into.password,into.phone,into.email,into.time,into.role))
                conn.commit()
                return True
    except Exception as e:
        print(f"错误{e}")






# if __name__=="__main__":
#     uvicorn.run(
#         "main:app",
#         host='127.0.0.1',
#         port=8000,
#         reload=True
#     )