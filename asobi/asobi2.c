#include<stdio.h>
int main(void){
    char str[3][10];
    int i;
    for (i = 0; i < 3; i++)
    {
        scanf("%s",str[i]);
        printf("%c\n",str[i][0]);
    }
    return 0;
}