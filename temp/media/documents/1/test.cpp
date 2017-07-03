#include <iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
    long n,k;
    cin>>n>>k;
    long long int arr[n];
    long long int ans[(n*(n-1))/2];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            ans[n*i+j-1] = abs(arr[i]-arr[j]);
        }
    }
    sort(ans,ans+((n*(n-1))/2));
    cout<<ans[k-1];
    return 0;
}

