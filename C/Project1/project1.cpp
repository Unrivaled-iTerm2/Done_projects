#include <stdio.h>
int main(void)
{
    typedef unsigned long long size_t;
    int input;
    scanf("%d", &input);
    for (size_t i = 0; i < input; i++)
    {
        printf("%d\n", i + 1);
    }
    return 0;
}