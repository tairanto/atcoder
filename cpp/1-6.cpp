#include <bits/stdc++.h>
using namespace std;
#define MAX_N 100

int main() {
  int n,a[MAX_N];
  scanf("%d", &n);
  //cout << n << endl;
  for (int i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
    //cout << a[i] << endl;
  }
  int ans[4] = {0,0,0,0};
  for (int i = 0; i < n; i++){
    for (int j = i+1; j < n;j++){
      for (int k = j+1; k < n;k++){
          //cout << i<< j<< k << endl;
          int len = a[i] + a[j] + a[k];
          int M = max(a[i], max(a[j], a[k]));
          if (len - M > M)
          {
              ans[0] = max(ans[0], len);
              ans[1], ans[2], ans[3] = a[i], a[j], a[k];
          }
      }
    }
  }
  cout << ans[0] << a[1] << a[2] << a[3] << endl;
}