my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # 副本赋予
friend_foods = my_foods # 指向指针
my_foods.append("ice")
friend_foods.append("cake")
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)