from fastapi import APIRouter,HTTPException
from db import sql_db
# from schemas import

router=APIRouter()

@router.get("/list",summary="评论内容")
async def get_com():
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select * from comment;"
            cursor.execute(sql)
            comments=cursor.fetchall()
            return comments
    except Exception as e:
        print(f"错误{e}")