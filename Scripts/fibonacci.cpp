#include <iostream>

using namespace std;

int fib(int f1, int f2, int n){
    if(n==1) return f2;
    return fib(f2,f2+f1,n-1);
}

int main(){
    int f1,f2,n; 
    cin >> f1 >> f2 >> n;
    cout << fib(f1,f2,n);
}
