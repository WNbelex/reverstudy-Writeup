a=[198,232,816,200,1536,300,6144,984,51200,570,92160,1200,565248,756,1474560,800,6291456,1782,65536000]
for i in range(1,len(a)+1):
    if ((i-1)%2==0):
        a[i-1]=a[i-1]/2**i
    else:
        a[i-1]=a[i-1]/i
    a[i-1]=int(a[i-1])
    a[i-1]=chr(a[i-1])
result = ''
for char in a:
    result += char

print(result)  # 输出: ctf2020{d9-dE6-20c}