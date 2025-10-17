"""不得不承认还是作者会玩，把flag藏在一个无名的小函数里面
不看csdn的wp我都不知道哪里找去
在假“主函数”里面，YOU FIND ME的位置下面，有一个byte开头的字符串，交叉引用进去
函数开始先对v1赋值，v1就是flag
 for ( i = 0; i <= 1233; ++i )
  {
    sub_40F790(v1);
    sub_40FE60();
    sub_40FE60();
    v1 = sub_40FE60() ^ 0x98765432;
  }
这块是混淆用的，不用搭理
 v4 = v1;
  if ( ((unsigned __int8)v1 ^ byte_6CC0A0[0]) == 'f' && (HIBYTE(v4) ^ (unsigned __int8)byte_6CC0A3) == 'g' )
  {
    for ( j = 0; j <= 24; ++j )
      sub_410E90(byte_6CC0A0[j] ^ *((_BYTE *)&v4 + j % 4));
  }
这段是主要的解密部分、
意思是把v1【0】和byte_6CC0A0【0】与v1【3】和byte_6CC0A0【3】异或的话，要是分别为f和g的话
就进行解密，可以猜测v4的前4位就是flag
byte_6CC0A0[j] ^ *((_BYTE *)&v4 + j % 4)
最关键的部分
我们先把flag异或成v1中的原始段（v1与byte_6CC0A0异或完才是flag）
我们只用到了v1的前四位  *((_BYTE *)&v4 + j % 4)==v1[j%4]
解出byte_6CC0A0[j] ^v1[j%4]
得到flag
"""
string=[73,111,100,108,62,81,110,98,40,111,99,121,127,121,46,105,127,100,96,51,119,125,119,101,107,57,123,105,121,61,126,121,76,64,69,67]
flag=""
for i in range(0,35):
    flag+=chr(string[i]^i)
print(flag)



data=[0x40, 0x35, 0x20, 0x56, 0x5D, 0x18, 0x22, 0x45, 0x17, 0x2F, 0x24, 0x6E, 0x62, 0x3C, 0x27, 0x54, 0x48, 0x6C, 0x24, 0x6E, 0x72, 0x3C, 0x32, 0x45, 0x5B]
four=['f','l','a','g']
data2=[]
data3=[]
flag=""
for i in range(4):
    data2.append(data[i]^ord(four[i]))   #两次异或等于没有异或
    data3.append(chr(data2[i]))
print(data3)
for i in range(len(data)):
    flag+=chr(data[i]^data2[i%4])
print(flag)