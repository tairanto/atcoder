#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

int H, W;
vector<vector<int>> field;

void dfs(int h,int w){
    field[h][w]=0;
    //8方向
    for (int dh = -1; dh < 2;dh++){
        for (int dw = -1; dw < 2;dw++){
            int nh = h + dh, nw = w + dw;

            if(nh<0||nh>=H||nw<0||nw>=W)continue;
            if (field[nh][nw]==0)continue;
            dfs(nh,nw);
        }
    }
}

//探索
int main(){
    while(cin>>W>>H){
        if (H==0||W==0) break;
        field.assign(H, vector<int>(W, 0));
        int count = 0;
        for (int h = 0; h < H; h++){
            for (int w = 0; w < W;w++){
                cin >> field[h][w];
            }
        }
        for (int h = 0; h < H; h++){
            for (int w = 0; w < W; w++){
                if (field[h][w] == 0)
                    continue;
                dfs(h, w);
                count++;
            }
        }
        cout << count << endl;
    }
}