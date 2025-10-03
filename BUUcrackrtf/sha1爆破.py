"""wp
无壳，ida打开
算了，直接看代码就行
学会了sha1加密，rtf文件前六位必然是'{\\rtf1'
"""



import hashlib
def sha1_encrypt(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()
# 测试示例
if __name__ == "__main__":
    # 要加密的文本
    for i in range(100000,999999):
        origin=str(i)+"@DBApp"
        passwd = sha1_encrypt(origin)
        if passwd == "6e32d0943418c2c33385bc35a1470250dd8923a9":#这里把ida里的大写变成小写
            print(origin)
            break
a2=[0x05, 0x7D, 0x41, 0x15, 0x26, 0x01]
rtf='{\\rtf1'
rtf=list(rtf)
for i in range(0,len(rtf)):
    rtf[i]=ord(rtf[i])
v5=6
flag=''
for i in range(0,6):
    flag+=chr(a2[i] ^ rtf[i])
print(flag)
#Flag{N0_M0re_Free_Bugs}
