def etp(string):
    new_str = ''
    count = 0
    index = 0
    while len(new_str) <= 30:
        if chr(ord(string[index])-len(string)+count*3) > 'a':
            new_str += chr(ord(string[index])-len(string)+count*3)
        else:
            new_str += str(ord('A')+(ord('A')-ord(string[index])-len(string)+count*3))
        if chr(ord(string[index])-len(string)+count*3) < 'z':
            new_str += chr(ord(string[index])-len(string)+count*3)
        else:
            new_str += str(ord('z')-(ord(string[index])-len(string)+count*3)-ord('z'))
        count += 1
        if index >=  len(string)-1:
            index = 0
        index += 1
    return str(new_str)

def check(string1, string2):
    if string1 == string2:
        return True
    else:
        return False

data = etp('asdas4')
print(check(etp('4asda'),data))
print(etp('s4'))
print(ord('a'))
print(ord('z'))

