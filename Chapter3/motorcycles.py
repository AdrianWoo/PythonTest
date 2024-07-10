motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1,'ducati')
print(motorcycles)

del motorcycles[1]  # 知道位置可以使用 del 关键字删除
print(motorcycles)

# pop方法 删除列表末尾的值

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# 知道索引位置删除元素
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# remove 只删除列表中出现的第一个值，如果需要多次删除，那么需要进行循环
motorcycles.remove('ducati')
print(motorcycles)
