import sqlite3

# 连接到数据库 如果数据库名称不存在, 则会自动创建并连接
con = sqlite3.connect(r'D:\Code\Python-Project-Practice\chapter3\test1.db')

cur = con.cursor()  # 创建游标对象
"""
cur.execute(sql) # 执行SQL语句
cur.execute(sql, parameters) # # 执行带参数的SQL语句
cur.executemany(sql, seq_of_parameters) # 根据参数执行多次SQL语句 
cur.executescript(sql_script) # 执行SQL脚本
"""
# 创建一个表
cur.execute("create table category (id primary key, sort, name)")
# 插入记录
cur.execute("insert into category values(1, 1, 'computer')")
# ?表示参数, 传递的参数使用元组
cur.execute("insert into category values(?, ?, ?)", (2, 3, 'literature'))
"""
获取游标的查询结果集
cur.fetchone(): 返回结果集的下行(Row对象), 无数据时返回None
cur.fetchall(): 返回结果集的剩余行(Row 对象列表), 无数据时返回空list
cur.fetchmany(): 返回结果集的多行(Row对象列表), 无数据时返回空list
"""
cur.execute("Select * from category ")
print(cur.fetchall())  # 提取查询到的数据

for row in cur.execute('select * from category'):
    print(row[0], row[1])

"""
数据库的提交和回滚
con.commit(): 事务提交
con.rollback(): 事务回滚
"""

"""
关闭Cursor对象和Connection对象
cur.close(): 关闭Cursor(游标)对象
con.close(): 关闭Connection对象
"""

