#include<iostream>

using namespace std;

int main(){
    int N;
    cin >> N;
    int cnt=0;
    for(int i=1;i<N+1;i+=2){
        int count=0;
        for(int j=1;j<i+1;j++){
            if (i%j==0)count++;
        }
        if(count==8)cnt++;
    }
    cout << cnt << endl;
}