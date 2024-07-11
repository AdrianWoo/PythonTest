def make_pizza(size, *toppings):
    """做披萨

    Args:
        size (int): 披萨的尺寸
        toppings: 披萨的配料
    """    
    print(f"\nMaking a {size}-pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(12, "pepperoni")
make_pizza(21, "mushrooms", "green peppers", "extra cheese")
