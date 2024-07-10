cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # sort 修改列表的排序是永久的
print(cars)

cars.sort(reverse=True)
print(cars)
print(sorted(cars))  # 临时排序
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse() # 列表反转 永久性
print(cars)

print(len(cars))
