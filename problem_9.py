import re 
from PIL import Image

img = Image.open('problem_9.png')
row = list()
for x in range(0, img.size[0], 7):
    row.append(img.getpixel((x, 45)))

ords = list()

for i in row:
    if i[0] == i[1] == i[2]:
        ords.append(i[0])

mes = list()
for i in ords:
    mes.append(chr(i))

# print(''.join(mes))
next_lvl = [105, 110, 116, 101, 103, 114, 105, 116, 121]

key = str()
for i in next_lvl:
    key = f'{key}{chr(i)}'

print(key)
# integrity