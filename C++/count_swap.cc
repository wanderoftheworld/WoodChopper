#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minSwaps(vector<int>&nums) {
    vector<pair<int,int>> v;
    for(int i=0;i<nums.size();i++) v.push_back({nums[i],i});
    sort(v.begin(),v.end());
    int count=0;
    for(int i=0;i<v.size();i++){
        if(v[i].second!=i){
            swap(v[i], v[v[i].second]);
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> nums = {10, 1, 4, 6, 7, 0};

    int result = minSwaps(nums);
    cout << "Total number of swaps: " << result << endl;

    return 0;
}
