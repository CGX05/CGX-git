from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from SqlConfig import sql_config
import json

app = FastAPI()

# 允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello():
    return {"hello world"}

# 取
@app.get("/get_stu")
async def get_students():
    con = sql_config()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * From students")
            result = cursor.fetchall()
        return {"data": result}
    finally:
        con.close()

# 写入新数据
@app.post("/post_stu")
async def post_students(id:str,name:str,clas:str,time:str,cre:str):
    con=sql_config()
    try:
        with con.cursor() as cursor:
            sql="INSERT INTO students VALUES(%s,%s,%s,%s,%s)"
            cursor.execute(sql,(id,name,clas,time,cre))
            con.commit()
    finally:
        con.close()

# 根据学号删除数据
@app.delete("/delete_stu")
async def delete_stu(id:str):
    con=sql_config()
    try:
        with con.cursor() as cursor:
            sql="DELETE FROM students WHERE STUDENT_ID = %s"
            cursor.execute(sql,(id))
            con.commit()
    finally:
        con.close()

# 改 根据字段改数据 条件为学号
@app.put("/put_stu")
async def put_stu(list:str,data:str,id:str):
    con=sql_config()
    try:
        with con.cursor() as cursor:
            if list=="NAME":
                sql="UPDATE students SET NAME=%s WHERE STUDENT_ID=%s"
            elif list=="CLASS":
                sql = "UPDATE students SET CLASS=%s WHERE STUDENT_ID=%s"
            elif list=="CREATOR":
                sql = "UPDATE students SET CREATOR=%s WHERE STUDENT_ID=%s"
            else:
                sql = "UPDATE students SET STUDENT_ID=%s WHERE STUDENT_ID=%s"
            cursor.execute(sql,(data,id))
            con.commit()
    finally:
        con.close()


