#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        map<int, int> map_count;
        int n = nums.size(), res = 0;

        for (int i = 0; i < n; i++)
            map_count[nums[i]] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int curr_diff = nums[j] - nums[i];
                if (curr_diff == diff) {
                    map_count[nums[j]]++;
                }
            }
        }

        for (auto it = map_count.begin(); it != map_count.end(); ++it) {
            if (map_count.count(it->first + diff) && it->first - diff > 0)
                res += it->second * map_count[it->first + diff];
        }

        return res;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {0, 1, 4, 6, 7, 10};

    int diff = 3;

    int result = solution.arithmeticTriplets(nums, diff);
    cout << "Total number of arithmetic triplets: " << result << endl;

    return 0;
}
