#include<stdio.h>
int main(){
  long n,q;
  scanf("%ld",&n);
  char s[2 * n + 1],s1[n],s2[n];
  scanf("%s",s);
  scanf("%ld",&q);
  
  int t;
  long a,b,i;
  char ai,bi;
  int count = 0;
  for(i = 0; i < q; i++){
    scanf("%d %ld %ld",&t,&a,&b);
    //printf("%d\n",t);
    if(t == 1){
      ai = s[a - 1];
      bi = s[b - 1];
      s[a - 1] = bi;
      s[b - 1] = ai;
      s[2 * n] = '\0';
      printf("1 %s\n",s);
    }
    
    if(t == 2){
      for(int j = 0; j < n; j++){
        s1[j] = s[j];
      }
      /*s1[i] = '\0';
      for(i = n; i < 2 * n; i++){
        s2[i - n] = s[i];
      }
      s2[i - n] = '\0';
      
      for(i = 0; i < n; i++){
        s[i] = s2[i];
        s[i + n] = s1[i];
      }*/
      //s[i + n] = '\0';
      //printf("2 %s\n",s);
    }
    
    count++;
  }
  printf("%s,%d\n",s,count);
  return 0;
}