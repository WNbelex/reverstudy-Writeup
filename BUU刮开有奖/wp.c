/* 
[--------------------writeup--------------------]
无壳，打开IDA
Main函数很简单，线索在DialogFunc里
发现关键字段string里，推测为flag
     if ( String[0] == v7[0] + 34
        && String[1] == v10
        && 4 * String[2] - 141 == 3 * v8
        && String[3] / 4 == 2 * (v13 / 9)
        && !strcmp(v4, "ak1w")
        && !strcmp(v5, "V1Ax") )
      {
        MessageBoxA(hDlg, "U g3t 1T!", "@_@", 0);
      }
    }
    由此段确认string猜测flag
    先看string【0】和【1】
    由v7和v10赋值，v7和v10经过初始化之后，经过sub_4010F0((int)v7, 0, 10)；
    （这里其实看不出来v10进了函数，打开sub_4010F0之后发现最初的for循环循环10次遍历一个字符串，才推出（我的不足））
    压根看不明白，直接丢vs，要改反编译代码，更改后把DialogFunc里定义的11个字符组成字符串丢进去，得到处理后的字符串
    字符串为   3CEHJNSZagn
    v7[0]='3' ascii为51 +34=85=‘U’=string[0]
    string[1]=v10='J'
    接着来看string[2-7]
     && !strcmp(v4, "ak1w")
        && !strcmp(v5, "V1Ax") )
    v4和v5都经过sub_401000((int)v18, strlen(v18))
    跟进函数，发现99%为基本代码，看不懂，发现byte_407830特殊
    双击进去发现为BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=
    即base64加密对“ak1w”和‘  V1Ax’进行base64解密
    得到string【2-7】
    拼接得到flag{UJWP1jMp}
*/

#include <stdio.h>
#include <string.h>

int __cdecl sub_4010F(char* a1, int a2, int a3)
{
    int result; // eax
    int i; // esi
    int v5; // ecx
    int v6; // edx

    result = a3;                                  // 10
    for (i = a2; i <= a3; a2 = i)
    {
        v5 =  i;
        v6 = a1[i];
        if (a2 < result && i < result)
        {
            do
            {
                if (v6 > a1[result])
                {
                    if (i >= result)
                        break;
                    ++i;
                    a1[v5] = a1[result];
                    if (i >= result)
                        break;
                    while (a1[i] <= v6)
                    {
                        if (++i >= result)
                            goto LABEL_13;
                    }
                    if (i >= result)
                        break;
                    v5 = 4 * i;
                    a1[result] = a1[i];
                }
                --result;
            } while (i < result);
        }
    LABEL_13:
        a1[result] = v6;
        sub_4010F0(a1, a2, i - 1);
        result = a3;
        ++i;
    }
    return result;
}

int mai(void)
{
    char str[] = "ZJSECaNH3ng";
    sub_4010F0(str, 0, 10);
    printf("%s", str);
    return 0;
}


