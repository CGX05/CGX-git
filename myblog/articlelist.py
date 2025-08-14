from fastapi import APIRouter,HTTPException
from db import sql_db

router=APIRouter()

@router.get("/list",summary="获取文章")
async def list():
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select * from article;"
            cursor.execute(sql)
            list=cursor.fetchall()
            return list
    except Exception as e:
        print(f"错误{e}")

@router.get("/data/{id}",summary="文章详情")
async def data(id:int):
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select * from article where id=%s;"
            cursor.execute(sql,(id,))
            list=cursor.fetchone()
            return list
    except Exception as e:
        print(f"错误{e}")