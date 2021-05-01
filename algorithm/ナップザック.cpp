#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[105][10009];
int x[105][10009];

int main(){
    int N,W;
    cin >> N >> W;
    for (int i = 0; i < N; i++)cin >> x[i][0] >> x[i][1];
    for (int i = 0; i < N;i++){
        for (int j = 0; j <= W;j++){
            if (x[i][1]<=j)dp[i+1][j]=max(dp[i][j-x[i][1]]+x[i][0],dp[i][j]);
            else dp[i+1][j]=dp[i][j];
        }
    }
    cout << dp[N][W] << endl;
}