#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // 使用当前时间作为随机数种子，确保每次运行结果不同
    srand(time(NULL));
    
    printf("生成5个随机整数：\n");
    for (int i = 0; i < 5; i++) {
        // 生成随机整数
        int random_num = random();
        printf("随机数 %d: %d\n", i + 1, random_num);
    }
    
    printf("\n生成5个1到100之间的随机整数：\n");
    for (int i = 0; i < 5; i++) {
        // 生成1到100之间的随机整数
        int random_range = 1 + (random() % 100);
        printf("随机数 %d: %d\n", i + 1, random_range);
    }
    
    return 0;
}
