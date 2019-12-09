import pymysql


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='wwh990325',
                       db='library'
                       )

cursor = conn.cursor()
sql = """DELETE FROM data
         """
cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()
