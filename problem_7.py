import zipfile
import re

pattern = r'\d+'

def problem(path: str, num: int, comments: str = str()) -> print:
    # path = f'{subpath}{num}.txt'
    with zipfile.ZipFile(path, 'r') as archive:
        text = str(archive.read(f'{num}.txt'))
        print(text)
        comment = archive.getinfo(f'{num}.txt').comment
        print(comment.decode('utf-8'))
        comments = comments + comment.decode('utf-8')
        reg = re.search(pattern, text)
        num = reg.group()
        print(comments)
        problem(path, num, comments)



problem('problem_7.zip', 90052)
# hockey