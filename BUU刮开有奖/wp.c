/* 
[--------------------writeup--------------------]
�޿ǣ���IDA
Main�����ܼ򵥣�������DialogFunc��
���ֹؼ��ֶ�string��Ʋ�Ϊflag
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
    �ɴ˶�ȷ��string�²�flag
    �ȿ�string��0���͡�1��
    ��v7��v10��ֵ��v7��v10������ʼ��֮�󣬾���sub_4010F0((int)v7, 0, 10)��
    ��������ʵ��������v10���˺�������sub_4010F0֮���������forѭ��ѭ��10�α���һ���ַ��������Ƴ����ҵĲ��㣩��
    ѹ���������ף�ֱ�Ӷ�vs��Ҫ�ķ�������룬���ĺ��DialogFunc�ﶨ���11���ַ�����ַ�������ȥ���õ��������ַ���
    �ַ���Ϊ   3CEHJNSZagn
    v7[0]='3' asciiΪ51 +34=85=��U��=string[0]
    string[1]=v10='J'
    ��������string[2-7]
     && !strcmp(v4, "ak1w")
        && !strcmp(v5, "V1Ax") )
    v4��v5������sub_401000((int)v18, strlen(v18))
    ��������������99%Ϊ�������룬������������byte_407830����
    ˫����ȥ����ΪBCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=
    ��base64���ܶԡ�ak1w���͡�  V1Ax������base64����
    �õ�string��2-7��
    ƴ�ӵõ�flag{UJWP1jMp}
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


