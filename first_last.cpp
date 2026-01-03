#include<iostream>
using namespace std;
int main(){
int n;
cin>>n;
int arr[n];
for(int i=0;i<n;i++){
    cin>>arr[i];
}
int target;
cin>>target;
int first,last = -1;
for(int i=0;i<n;i++){
    if(arr[i]==target){
        if(first==-1)
            first=i;
        last=i;
    }
    
}
if (first==-1)
    cout<<-1;
else
    cout<<first<<" "<<last;
return 0;
}