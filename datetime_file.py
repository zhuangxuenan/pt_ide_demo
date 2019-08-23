from datetime import datetime, timedelta

# datetime
t1 = datetime.now()  # 当前时间 2019-08-14 16:05:41.923949
# timestamp
t2 = t1.timestamp() * 1000  # 时间毫秒值 1565769941923
# datetime
t3 = datetime(2019, 8, 14, 15, 42, 30)  # 年月日时分秒 指定时间 2019-08-14 15:42:30
# timestamp
t4 = t3.timestamp() * 1000  # 时间毫秒值 1565768550000
# datetime
t5 = datetime.fromtimestamp(t2 / 1000)  # 将时间戳重新格式化为时间格式 2019-08-14 16:05:41.923949
# str转换为datetime
t6 = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# datetime转换为str
t7 = t1.strftime('%a, %b %Y-%m-%d %H:%M:%S')
# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符
t8 = t1 - timedelta(hours=10)  # 往前倒退10个小时
t9 = t1 - timedelta(days=1)  # 往前倒退1天、
t10 = t1 - timedelta(days=1, hours=1)  # 往前倒退一天零1小时
print(t1)
print(int(t2))
print(t3)
print(int(t4))
print(t5)
print(t6)
print(t7)
print(t8, ' ', t9, ' ', t10)
