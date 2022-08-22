#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n = 1000000;
    int *a = calloc(n, sizeof(int));
    int *b = calloc(n, sizeof(int));

    for (int i = 0; i < n; i++)
    {
        *(a + i) = i;
        *(b + i) = i;
    }

    int *res = calloc(n, sizeof(int));

    for (int i = 0; i < n; i++) {
        *(res + i) = *(a + i) * *(b + i);
    }

    for (int i = 0; i < 10; i++) {
        printf("%d\n", *(res + i));
    }
    return 0;
}
