#include<stdio.h>

int main(void){
 int n,i,j;
 scanf("%d",&n);
 
 int a[n][2];
 for(i = 0; i < n ;i++){
    for(j = 0; j < 2 ;j++){
       scanf("%d",&a[i][j]);
    }
 }

 for(i = 1; i < n ;i++){
    if(a_min > a[i][0]){
      a_min = a[i][0];
      a_ban = i;
    }
 }
 for(i = 1; i < n ;i++){
     if(b_min > a[i][1]){
        if(a_ban == i)continue;
        b_min = a[i][1];
    }
 }

 if(a_min + a[a_ban][1] < b_min){
    printf("%d\n",a_min + a[a_ban][1]);
 }else{
   if(a_min > b_min){
     printf("%d\n",a_min);
   }else if(b_min > a_min){
     printf("%d\n",b_min);
   }
 }
 return 0;

}