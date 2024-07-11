class Dog:
    """一次简单的小狗尝试"""
    def __init__(self,name,age):
        """初始化属性

        Args:
            self 是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
            name (string): 名称
            age (int): 年龄
        """
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("Haha",6)
my_dog.sit()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
