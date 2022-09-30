#include<stdio.h>

int add(int a, int b)
{
    int s = a + b;
    return s;
}

int main()
{
    int sum = add(5, 7);
    printf("%d\n", sum);
    return 0;
}