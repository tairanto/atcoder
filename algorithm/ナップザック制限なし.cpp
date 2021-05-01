#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[105][10009];
int x[105][10009];

int main(){
    int N,W;
    cin >> N >> W;
    int m=100000;
    for (int i = 0; i < N; i++){
        cin >> x[i][0] >> x[i][1];
        m = min(m, x[i][1]);
    }
    for (int j = 0; j <= W; j++){
        for (int i = 0; i < N; i++){
            if (x[i][1]<=j)dp[i+1][j]=max(dp[i+1][j-x[i][1]]+x[i][0],dp[i][j]);
            else dp[i+1][j]=dp[i][j];
        }
    }
    cout << dp[N][W] << endl;
}