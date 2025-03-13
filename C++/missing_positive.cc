#include <vector>
#include <iostream>

using namespace std;

class Solver {
  public:
  static int firstMissingPositive(vector<int>& arr) {
    int n = arr.size();

    int i = 0;
    while (i < n) { 
      if (arr[i] > 0 && arr[i] <= n) {
        int pos = arr[i] - 1;
        if (pos != i) {
          int next = arr[pos];
          arr[pos] = i + 1;
          while (next > 0 && next <= n) {
            int temp = arr[next - 1];
            arr[next - 1] = next;
            temp = next;
          }
        }
      }
    }

    for (int i=0; i<n; i++) {
      if (arr[i] != i+1) return i + 1;
    }
    return n;
  }
};

int main() {
    vector<int> nums = {2, 1, 4, 6, 7, 0};

    cout << "First missing positive is: " << Solver::firstMissingPositive(nums) << endl;

    return 0;
}

