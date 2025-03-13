#include <vector>
#include <iostream>

using namespace std;

int firstMissingPositive(vector<int>& arr) {
    int n=arr.size();
    int i=0;
    while(i<n){
        if(arr[i]==i+1){
            i++;
        }
        else if (arr[i]>=1 && arr[i]<=n){
            if(arr[i]==arr[arr[i]-1]){
                i++;
            }
            else{
                swap(arr[i],arr[arr[i]-1]);
            }
        }
        else{
            i++;
        }
    }
    for(int i=0;i<n;i++){
        if (arr[i]!=i+1){
            return i+1;
        }
    }
    return n+1;
}

int main() {
    vector<int> nums = {10, 1, 4, 6, 7, 0};

    int result = firstMissingPositive(nums);
    cout << "First missing positive is: " << result << endl;

    return 0;
}

