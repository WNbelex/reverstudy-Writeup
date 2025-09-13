#用于动态代码

text = "e3nifIH9b_C@n@dH"
ascii_list = [ord(c) for c in text]
print(ascii_list)
for i in range(0, len(ascii_list)):
    ascii_list[i] = ascii_list[i] - i
print(ascii_list)
txt=[chr(c) for c in ascii_list]
print(txt)
word=str(txt)
print(word)