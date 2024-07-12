from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
      return None
  
def stored_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"We'll remember you when you come back, {username}!")
    else:
        username = stored_username(path)
        print(f"We'll remember you when you come back, {username}!")
    
greet_user()