#include <bits/stdc++.h>
using namespace std;
#define MAX_N 100

int main() {
  stack<int> s;
  s.push(1);
  s.push(100);
  printf("%d\n", s.top());
  s.pop();
  printf("%d\n", s.top());
}