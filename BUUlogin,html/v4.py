'''writeup
题目是一个HTML文件，用浏览器打开之后很简单
f12检查，在body里面发现了加密逻辑
但是主包看不懂JavaScript代码，只能请ai来分析下
能看出将我们输入的内容处理之后与
PyvragFvqrYbtvafNerRnfl@syner-ba.pbz进行相等比较
                if ("PyvragFvqrYbtvafNerRnfl@syner-ba.pbz" == rotFlag) {
                    alert("Correct flag!");
                } else {
                    alert("Incorrect flag, rot again");
                }
问过ai之后发现是ROT13加密，用CSDN里的大佬给的代码解密之后得到flag
（是个纯签到题）
flag{ClientSideLoginsAreEasy@flare-on.com}
'''

enc = input("输入待解密内容：")
flag = ''
for i in enc:
    if ord(i) >= 65 and ord(i) <= 90:
        if ord(i) - 13 < 65 :
            flag += chr(ord(i) + 13)
        else:
            flag += chr(ord(i) - 13)
    elif ord(i) >= 97 and ord(i) <= 122:
        if ord(i) - 13 < 97 :
            flag += chr(ord(i) + 13)
        else:
            flag += chr(ord(i) - 13)
    else:
        flag += i

print(flag)




















