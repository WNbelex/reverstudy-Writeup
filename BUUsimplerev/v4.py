"""writeup"""
"""32位无壳，
IDA发现关键函数Decry
关键句if ( !strcmp(text, str2) )
text：由AL计算为killshadow"""
#str2由输入语句和key计算得出，经过以下代码爆破，反推出输入语句
#得到flag{KLDQCUDFZO}


#用于动态代码
text = 'killshadow'
key = 'adsfkndcls'
A=range(ord("A"),ord("Z")+1)
print(A)
flag = ''
v3 = 10
v5 = len(key)
#flag经过运算变为killshadow
for i in range(0,10):
    for j in A:
            if text[i] == chr((j - 39 - ord(key[v3 % v5]) + 97) % 26 + 97):
                flag = flag + chr(j)
                v3 = v3 + 1
                print('success', flag)
                break
print(flag)



# if j == " ":
#     flag = flag + j
# if (j<ord('A') or j>ord('Z')):
#     continue
#     if ('`' < A[i] < "{"):
#         if text[i]==chr(( j - 39 - key[v3 % v5] + 97) % 26 + 97):
#             v3=v3+1
#             flag=flag+text[i]
#             print('success',flag)
#             break
#         else:
#             print('error')
# else :