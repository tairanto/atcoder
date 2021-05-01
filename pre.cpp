#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;
int main()
{
    long long mod = pow(10,9) + 7;
    long long n, p;
    cin >> n >> p;
    long long ans = p - 1;
    for (int i=0;i<n-1;i++){
        ans = (ans * (p - 2)) % mod;
    }
    cout << ans << endl;
}