a = input("Nhap chuoi nhi phan: ")
c = [x for x in a.split(" ")]
b= []

for i in c:
    b.append(int(i,2))
print(b)
decode = []
for i in b:
    decode.append(chr(i))
print(decode)

d = [x for x in input("Nhap chuoi Oc: ").split(" ")]
def listtostr(s):
    str1 = ""
    for i in s:
        str1 += chr(int(i,8))
    return str1
print(listtostr(d))

hex1 = [x for x in input("nhap chuoi hex: ").split(" ")]

def hextostr(s):
    str2 = ""
    for i in s:
        str2 += chr(int(i,16))
    return str2
print(hextostr(hex1))
    