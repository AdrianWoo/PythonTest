def greet_users(names):
    """每个用户问候"""
    for name in names:
        msg = f'Hello {name.title()}!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)