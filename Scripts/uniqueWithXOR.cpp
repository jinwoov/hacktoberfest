/** The problem statement is: Find a number which occurs only once in a array when all other appear twice.
    This implies that size of array is odd.
    We shall be using the properties of XOR to find the no as: 
    1. a XOR a = 0
    2. 0 XOR b = b
**/

#include<iostream>
using namespace std;

int unique(int *arr, int n) {
    int ans = arr[0];
    for(int i = 1; i < n; i++) {
        ans = ans ^ arr[i];
    }
    return ans;
}
int main() {
    int n;
    cin>>n;                                      //taking size of the array 
    int *arr = new int[n];
    for(int i = 0; i < n; i++) {                 //input the array elements
        cin>>arr[i];
    }
    cout<<unique(arr, n)<<endl;
    return 0;
}