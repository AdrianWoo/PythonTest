name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
message1 = f"Hello {name.title()}, would you like to learn some Python today?"
message2 = f"Hello {name.upper()}, would you like to learn some Python today?"
message3 = f"Hello {name.lower()}, would you like to learn some Python today?"
print(message)
print(message1)
print(message2)
print(message3)

femost = "Albert Einstein"
message4 = f'{femost} once said, "A person who never made a mistake never tried anything new."'
print(message4)


femost1 = "   \t   Albert Einstein         \n "
print(femost1)
print(femost1.rstrip())
print(femost1.lstrip())
print(femost1.strip())

filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))
