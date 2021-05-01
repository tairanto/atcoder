#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;
using Graph = vector<vector<int>>;

vector<bool> seen;
vector<int> first_order; // 行きがけ順
vector<int> last_order;  // 帰りがけ順

void dfs(const Graph &G, int v, int &ptr){
    // 行きがけ順をインクリメントしながらメモ
    first_order[v] = ptr++;

    seen[v] = true;
    for (auto next_v : G[v])
    {
        if (seen[next_v])
            continue;
        dfs(G, next_v, ptr);
    }

    // 帰りがけ順をインクリメントしながらメモ
    last_order[v] = ptr++;
}

int main(){
    // 頂点数と辺数
    int N;
    cin >> N ;

    // グラフ入力受取 (ここでは無向グラフを想定)
    Graph G(N);
    for (int i = 0; i < N; ++i){
        int a, b ;
        cin >> a >> b;
        for (int j = 0; j < b;j++){
            int c;
            cin >> c;
            G[a-1].push_back(c-1);
        }   
    }

    // 頂点 0 をスタートとした探索
    seen.assign(N, false); // 全頂点を「未訪問」に初期化
    first_order.resize(N);
    last_order.resize(N);
    int ptr=0;
    for (int v = 0; v < N;v++){
        if (seen[v])
            continue;
        dfs(G, v, ptr);
    }

    // 各頂点 v の行きがけ順、帰りがけ順を出力
    for (int v = 0; v < N; ++v)
        cout << v+1 << " "<< first_order[v]+1 <<" "<< last_order[v]+1 << endl;
}