import pymysql
def adduser():
    db = pymysql.connect(host="localhost", user="root",password="654321",database="test",charset="utf8")
    cursor = db.cursor()
    sql = "insert into dates values(now())"
    try:
        cursor.execute(sql)
        db.commit()
        return {"result": "ok"}
    except:
        db.rollback()
        return {"result": "error"}
    db.close()
mss = adduser()