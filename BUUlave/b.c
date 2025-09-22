/*writeup
不是pe文件，直接ida打开
分析main函数代码，发现函数读取了flag文件，我们没有
但是给了我们flag在经过计算之后的txt文件，
计算的过程是，对索引i为基数的元素左移i位（移位运算）
对索引i为偶数的元素乘i
直接写出我们的反计算代码啊
把flag算回来*/
#include <stdio.h>
#include <stdint.h>
int main() {
    // 给定的输出（output.txt）
    int outputs[] = {
        198, 232, 816, 200, 1536, 300, 6144, 984, 51200, 570,
        92160, 1200, 565248, 756, 1474560, 800, 6291456, 1782, 65536000
    };

    char flag[21] = { 0 }; // 索引 0 未使用，我们只填充 1~19，最后加 \0

    for (int i = 1; i <= 19; i++) {
        int out = outputs[i - 1];
        int8_t schar_val;

        if (i & 1) { // 奇数情况
            schar_val = out >> i;
        }
        else {     // 偶数情况
            schar_val = out / i;
        }

        // 将 schar_val 转为 unsigned char 存入 flag[i]
        flag[i] = schar_val;
        printf("%d\n", flag[i]);
    }

    // 打印 flag（从索引 1 开始）
    printf("Flag: ");
    for (int i = 1; i <= 19; i++) {
        printf("%c", flag[i]);
    }
    printf("\n");

    return 0;
}


