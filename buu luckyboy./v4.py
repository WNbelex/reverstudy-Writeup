"""writeup"""
"""main函数里只有patchme（v4）剩下都是没有用·
下面发现get——flag（）
点进去
在case1中发现flag由f1和f2拼接，f1为GXY{do_not_能看出为flag的一部分
f2是空的，继续向下找
发现在case4中
   s = 0x7F666F6067756369LL;（知识点：可转换为[0x69,0x63,0x75,0x67,0x60,0x6F,0x66,0x7F]
   也可转为python代码中的v2）
strcat(&f2, (const char *)&s);
f2被赋值
在case5中
f2被运算
用代码重现该过程
得到v2最终的模样
hate_me}
拼接得到
GXY{do_not_hate_me}
在buu中为flag{do_not_hate_me}
"""


v2=[127,102,111,96,103,117,99,105]
v2.reverse()
a=0
while a<1:
    for j in range(0,len(v2)):
        if (j % 2 == 1):
            v2[j]=v2[j]-2
        else:
            v2[j]=v2[j]-1
    a=a+1
v2t=[]
for j in range(0,len(v2)):
    print(chr(v2[j]))



























