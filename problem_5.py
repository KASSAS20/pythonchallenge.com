import urllib.request
import re
num = 12345
pattern = r'nothing is \d+'
pattern_num = r'\d+'
for i in range(400):
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={num}'  # Замените это на целевой URL
    response = urllib.request.urlopen(url)

    # Чтение и вывод содержимого ответа
    # num = str(response.read()).replace('and the next nothing is ', '')
    subnum = (str(response.read()))
    print(subnum)
    if 'Yes. Divide by two and keep going.' in subnum:
        num = int(num)/2
    else:
        try:
            reg_0 = re.search(pattern, subnum)
            reg = re.search(pattern_num, reg_0.group())
            num = reg.group()
        except:
            content = response.read() 
            print(content.decode('utf-8'))
    print(num)

# peak.html
