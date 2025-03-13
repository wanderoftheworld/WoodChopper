#include<iostream>
using namespace std;
typedef long long ll;
double pi = acos(-1);
const int maxn = 2e5 + 10;
const ll P = 1145141919;
const double eps = 1e-8;
void solve() {
  int n,ans=0;
  cin >> n;
  vector<double>x(n + 1), y(n + 1);
  for (int i = 1; i <= n; i++) {
    cin >> x[i] >> y[i];
  }
  for (int i = 1; i <= n-2; i++) {
    if (x[i + 1] - x[i] > 0 && y[i + 2] - y[i + 1] > 0) ans++;
    if (y[i + 1] - y[i] < 0 && x[i + 2] - x[i + 1] > 0) ans++;
    if (x[i + 1] - x[i] < 0 && y[i + 2] - y[i + 1] < 0) ans++;
    if (y[i + 1] - y[i] > 0 && x[i + 2] - x[i + 1] < 0) ans++;
  }
  cout << ans << '\n';
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t = 1;
  cin >> t;
  solve();
  return 0;
}
