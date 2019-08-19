import random
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
import string

conn = sqlite3.connect('D:\py_img\person.db')
# 创建一个cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(30) primary key,name varchar(30))')
# 插入100条数据数据
for i in range(100):
    # 随机生成五个字符 然后组装成一个字符串 首字母大写
    str_s = "".join(random.sample(string.ascii_letters, 5)).capitalize()
    print(str_s)
    cursor.execute(
        'insert into user (id, name) values (\'%s\', \'%s\')' % (str(i + 1), str_s))
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
