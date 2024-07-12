from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('E:/SourceCode/PythonTest/Chapter10/programing.txt')
path.write_text(contents)