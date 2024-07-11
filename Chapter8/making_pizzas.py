import pizza  # 导入整个模块
import pizza as p # 导入整个模块 并设置别名
from pizza import * # 导入整个模块 中的所有方法 -- 非自己写的不建议
from pizza import make_pizza # 导入模块中的某个方法
from pizza import make_pizza as mp # 导入模块中某个方法，并设置别名

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')