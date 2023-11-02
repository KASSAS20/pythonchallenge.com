alphabet = list("abcdefghijklmnopqrstuvwxyz")


def cesar(messasge: str) -> print:
    result = str()
    ignor = list('. ()yz')
    for char in messasge:
        char = char.lower()
        if char not in ignor: 
            a = ord(char)
            result += chr(a+2)
        elif char == 'y':
            result+='a'
        elif char == 'z':
            result+='b'
        else:
            result+=char
            
    print(result)



cesar('''G FMNC WMS BGBLR RPYLQJYRC GR ZW FYLB. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.''')
cesar('map')
# ocr
