"""writeup
第一次遇到带UPX壳的
在kali中upx -d exe脱壳
IDA打开
 {
    if ( v4[i] != _data_start__[*((char *)v5 + i) - 1] )
      return 0;
  }
主函数的关键判断句
把这个看懂好难555，其实看的关键在于_data_start__之后的中括号
这块看出来就可以把[*((char *)v5 + i) - 1]看成[j]     //谢谢大佬的wp
*((char *)v5 + i) - 1实际上是一个索引，我们不知道v5【i】-1的具体值，所以要算出来，我们把v5【i】-1设为j
j=v5[i]-1
v5[i]=j+1
以v4[0]为例，有v4[0]="*"=_data_start_[84],则v5[0]-1=84
v5[0]=chr(85)="U"
那么v5这个数组即为flag{U9X_1S_W6@T?}
这个我推算好久，还是太菜了
"""
key = '~}|{zyxwvutsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(\'&%$# !"'
encrypt = [42,70,39,34,78,44,34,40,73,63,43,64]
v5 = []
flag = ''
for i in encrypt:
  v5.append(key.find(chr(i))+1)
  print(ord(key[i]))
for i in v5:
  flag += chr(i)
print(flag)
print(chr(85))




















