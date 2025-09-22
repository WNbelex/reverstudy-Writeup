/*writeup
����pe�ļ���ֱ��ida��
����main�������룬���ֺ�����ȡ��flag�ļ�������û��
���Ǹ�������flag�ھ�������֮���txt�ļ���
����Ĺ����ǣ�������iΪ������Ԫ������iλ����λ���㣩
������iΪż����Ԫ�س�i
ֱ��д�����ǵķ�������밡
��flag�����*/
#include <stdio.h>
#include <stdint.h>
int main() {
    // �����������output.txt��
    int outputs[] = {
        198, 232, 816, 200, 1536, 300, 6144, 984, 51200, 570,
        92160, 1200, 565248, 756, 1474560, 800, 6291456, 1782, 65536000
    };

    char flag[21] = { 0 }; // ���� 0 δʹ�ã�����ֻ��� 1~19������ \0

    for (int i = 1; i <= 19; i++) {
        int out = outputs[i - 1];
        int8_t schar_val;

        if (i & 1) { // �������
            schar_val = out >> i;
        }
        else {     // ż�����
            schar_val = out / i;
        }

        // �� schar_val תΪ unsigned char ���� flag[i]
        flag[i] = schar_val;
        printf("%d\n", flag[i]);
    }

    // ��ӡ flag�������� 1 ��ʼ��
    printf("Flag: ");
    for (int i = 1; i <= 19; i++) {
        printf("%c", flag[i]);
    }
    printf("\n");

    return 0;
}


