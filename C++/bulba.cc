#include <vector>
#include <iostream>

using namespace std;

int maxSubArraySum(const std::vector<int>& nums) {
    int max_so_far = nums[0], max_ending_here = nums[0];

    for (int i = 1; i < nums.size(); i++) {
        max_ending_here = std::max(nums[i], max_ending_here + nums[i]);
        max_so_far = std::max(max_so_far, max_ending_here);
    }

    return max_so_far;
}

int main() {
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

    int result = maxSubArraySum(nums);
    cout << "Result: " << result << endl;

    return 0;
}
