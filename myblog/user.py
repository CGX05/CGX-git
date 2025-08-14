from fastapi import APIRouter,HTTPException,Depends,status
from jwt import ExpiredSignatureError,PyJWTError
import jwt
from fastapi.security import OAuth2PasswordBearer
from db import sql_db
import schemas
from schemas import users
from fastapi.responses import JSONResponse


router=APIRouter()

secret_key = 'pmiqgtNFFVagSB7DZPPoir7Hb7g25qH1eSiou5fqP5s'
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def verify_token_expiration(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token 无效或已过期",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret_key, algorithms=ALGORITHM)
        return True  # token 有效
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token 已过期",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except PyJWTError:
        raise credentials_exception

@router.get("/users",summary="获取用户")
async def read_user(is_valid:bool=Depends(verify_token_expiration)):
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select id,username,password,phone,emali,time from user;"
            cursor.execute(sql)
            user=cursor.fetchall()
            return user
    except Exception as e:
        print(f"操作错误{e}")

@router.post("/up_user",summary="更新用户")
async def updata(upuser:users,is_valid:bool=Depends(verify_token_expiration)):
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql='update user set username=%s,password=%s,phone=%s,emali=%s where id=%s;'
            cursor.execute(sql,(upuser.username,upuser.password,upuser.phone,upuser.emali,upuser.id))
            conn.commit()
            return JSONResponse(content={"success": True, "message": "修改成功"}, status_code=200)
    except Exception as e:
        print(f"错误{e}")

@router.delete("/del_user",summary="删除用户")
async def deldata(user_id:int,is_valid:bool=Depends(verify_token_expiration)):
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="delete from user where id=%s;"
            cursor.execute(sql,(user_id))
            conn.commit()
            return JSONResponse(content={'success':True},status_code=200)
    except Exception as e:
        print(f"错误{e}")

