#include <stdio.h>

int main()
{
    int a[] = {1, 2, 3, 4, 5};

    for (int i = 0; i < sizeof(a) / sizeof(int); i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");

    for (int i = 0; i < sizeof(a) / sizeof(int); i++)
    {
        printf("%d ", *(a + i));
    }
    printf("\n");
}

// 1 2 3 4 5
// 1 2 3 4 5