#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int arithmeticTriplets(vector<int>& nums, int diff) {
    int n = nums.size(), res = 0;
    vector<int> cnt(n);
    unordered_map<int, int> f;

    for(int i = 0; i < n; i++) {
        if(f.find(nums[i] - diff) != f.end()) {
            cnt[i] += f[nums[i] - diff];
        }
        f[nums[i]]++;
    }

    f.clear();
    for(int i = n - 1; i >= 0; i--) {
        if(f.find(nums[i] + diff) != f.end()) {
            res += cnt[i] * f[nums[i] + diff];
        }
        f[nums[i]]++;
    }

    return res;
}

int main() {
    vector<int> nums = {0, 1, 4, 6, 7, 10};

    int diff = 3;

    int result = arithmeticTriplets(nums, diff);
    cout << "Total number of arithmetic triplets: " << result << endl;

    return 0;
}
