responses = {}

polling_active = True

while polling_active:
    name = input("\t what's your name?")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repet = input('Would you like to let another person respond? (yes/no)')

    if repet == 'no':
        polling_active = False
    
print("\t-----Poll Result")

for name,response in responses.items():
    print(f"{name} would like to climb {response}.")