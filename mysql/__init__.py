# coding: utf-8
import MySQLdb

# 连接数据库
conn = MySQLdb.connect(host="localhost", user="root", passwd="123", db="PythonStudy", port=3306, charset="utf8")

# 获得游标
cur = conn.cursor()

"""
操作数据库
"""


try:
    # 插入
    cur.execute("insert into test(name_1, age) VALUES (%s, %s)",  ("python", 18))
    # 更新
    cur.execute("update test set name_1 = %s where age = %s", ("study", 18))
    # 删除
    cur.execute("delete from test where age = %s", (18,))

    # 提交事务
    conn.commit()
except Exception as e:
    print e
    # 回滚
    conn.rollback()


# 查询
cur.execute("select * from test")
# 总共多少条记录
print cur.rowcount
# 获取一条数据
rs = cur.fetchone()
print rs
# 获取多条数据
rs = cur.fetchmany(2)
for row in rs:
    print "name=%s, age=%d" % row
# 获取剩下所有的数据
rs = cur.fetchall()
print rs

# 关闭游标
cur.close()
# 关闭连接
conn.close()

