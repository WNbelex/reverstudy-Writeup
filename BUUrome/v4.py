'''writeup
庆祝我第一个独立不看writeup解出来的flag
虽然很简单，但我觉得这是我前进的一大步
ok，进正题
程序为32位无壳，ida直接开
main函数里有两个函数
分别点进，func函数就是我们熟悉的页面了
程序末尾的判别是v12（result）和v1的比较，其中v12已经告诉我们了
v1就是我们要找的flag
对v1的处理为
 for ( i = 0; i <= 15; ++i )
              {
                if ( *((char *)v1 + i) > 64 && *((char *)v1 + i) <= 90 )
                  *((_BYTE *)v1 + i) = (*((char *)v1 + i) - 51) % 26 + 65;
                if ( *((char *)v1 + i) > 96 && *((char *)v1 + i) <= 122 )
                  *((_BYTE *)v1 + i) = (*((char *)v1 + i) - 79) % 26 + 97;
              }
就是如果是大写字母改一下，是小写字母改一下
都不是就不改
那我们就直接反写个脚本把它炸出来啊
直接getflag{Cae3ar_th4_Gre@t}

'''



v12="Qsw3sj_lz4_Ujw@l"
flag=[]
a=[]
for i in range (55,150):
    a.append(i)
for j in range(0,len(v12)):
    found = False  #判断v1里不是字母的情况
    for k in range(0,len(a)):
            if 91>a[k]>=64:
                if v12[j]==chr((a[k]-51)%26+65):
                    flag.append(chr(a[k]))
                    found = True
                    break
            elif 97<=a[k]<=122:
                if v12[j]==chr((a[k]-79)%26+97):
                    flag.append(chr(a[k]))
                    found = True
                    break
    if not found: #学到新代码了
        flag.append(v12[j])

flag_str = ''.join(flag)   # 列表转字符串
print(flag_str)




















