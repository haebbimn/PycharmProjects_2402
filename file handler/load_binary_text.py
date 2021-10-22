with open('text.txt', 'wb') as f:
    f.write(b'\xea\xb0\x80')

input()
with open('text.bin', 'r',encoding='utf-8') as f:
    data = f.read()
print(data)