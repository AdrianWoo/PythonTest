from pathlib import Path

def word_count(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
    

file_path = ['alice.txt','little_women.txt','moby_dick.txt','heidado.txt']
for filepath in file_path:
    whole_path = f"E:/SourceCode/PythonTest/Chapter10/{filepath}"
    path = Path(whole_path)
    word_count(path)
