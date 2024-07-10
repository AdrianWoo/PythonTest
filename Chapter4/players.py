players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) # 不指定索引，从头开始切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) # 不指定结尾，切片到头

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) # 使用负数，打印后三个的


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:-3]) # 使用负数，打印从头到后几个为止


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")

for player in players[:3]: # 打印前三个
    print(player.title())