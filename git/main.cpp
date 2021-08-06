#include "sorting.h"
#include<iostream>
#include<vector>
using namespace std;
int main(){
int n;
cin>>n;
vector<int>p;
 vector<int>q;
for(int i=0;i<n;i++){
int k;
cin>>k;
p.push_back(k);
}
q=sort_custom(p);
 for(int z=0;z<q.size();z++){
   cout<<q[z]<<" ";
 }
 cout<<endl;
 return 0;
}
