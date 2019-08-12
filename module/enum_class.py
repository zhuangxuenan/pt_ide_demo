from enum import Enum, unique

# 枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数。


# Enum派生自定义类
@unique
class WeekDay(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 调用方式
print('--------------', WeekDay.Sun)
print('--------------', WeekDay['Sun'])
print('--------------', WeekDay.Sun.value)
# 实体类中如果某些属性的取值是固定的话可以使用定义枚举类赋值
