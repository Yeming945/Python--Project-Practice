""" 创建数据库和表 """
import sqlite3
con = sqlite3.connect(r'D:\Code\Python-Project-Practice\chapter3\test2.db')

con.execute('create table book(id primary key, price, name)')

books = [('021', 25, '大学计算机'), ('022', 30, '大学英语'),
         ('023', 18, '艺术欣赏'), ('024', 35, '高级语言程序设计'), ]
cur = con.cursor()

# 插入一行数据
cur.execute(
    "insert into book(id, price, name) values('001', 33, '大学计算机多媒体')"
)
cur.execute(
    "insert into book(id, price, name) values(?, ?, ?)", ('002', 28, '数据库基础')
)

# 插入多行数据
cur.executemany("insert into book(id, price, name) values(?, ?, ?)", books)

# 修改一行数据
cur.execute("update book set price=? where name=?", (25, "大学英语"))

# 删除一行数据
n = cur.execute("delete from book where price=?", (25,))

# 查询数据
cur.execute('select id, price, name from book')
for row in cur:
    print(row)

print('删除了', n.rowcount, '行记录')
con.commit()
cur.close()
con.close()

