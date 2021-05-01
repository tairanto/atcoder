#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using Graph = vector<vector<int>>;

vector<long long> color;
vector<long long> ans;
int a, b;

int main()
{
    // 頂点数と辺数
    int N;
    cin >> N;
    color.assign(N,0);
    ans.assign(N, 0);
    for (int i = 0; i < N;i++)cin >> color[i]
        // グラフ入力受取 (ここでは無向グラフを想定)
        Graph G(N);
    for (int i = 0; i < N - 1; i++)
    {
        cin >> a >> b;
        G[a - 1].push_back(b - 1);
        G[b - 1].push_back(a - 1);
    }

    // BFS のためのデータ構造
    vector<int> dist(N, -1); // 全頂点を「未訪問」に初期化
    queue<int> que;

    // 初期条件 (頂点 0 を初期ノードとする)
    dist[0] = 1;
    que.push(1); // 0 を橙色頂点にする

    // BFS 開始 (キューが空になるまで探索を行う)
    while (!que.empty())
    {
        int v = que.front(); // キューから先頭頂点を取り出す
        que.pop();

        // v から辿れる頂点をすべて調べる
        for (int nv : G[v])
        {
            if (dist[nv] != -1)
                continue; // すでに発見済みの頂点は探索しない

            // 新たな白色頂点 nv について距離情報を更新してキューに追加する
            dist[nv] = dist[v] + 1;
            que.push(nv);
        }
    }

    // 結果出力 (各頂点の頂点 0 からの距離を見る)
    for (int v = 0; v < N; ++v)
        cout << v << ": " << dist[v] << endl;
}