# 获取系统信息
import psutil

print(psutil.cpu_count())  # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心
# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())
# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for i in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))
# 获取物理内存
print(psutil.virtual_memory())
print(psutil.swap_memory())
# 磁盘分区、磁盘使用率和磁盘IO信息：
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())  # 获取网络接口信息
print(psutil.net_if_stats())  # 获取网络接口状态
print(psutil.net_connections())  # 获取当前网络连接信息
