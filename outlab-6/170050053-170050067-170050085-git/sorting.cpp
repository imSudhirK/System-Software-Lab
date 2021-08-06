#include<iostream>
#include<vector>
#include "sorting.h"
using namespace std;
vector<int> sort_custom(vector<int>r){
  for(int i=0;i<r.size();i++){
    for(int j=r.size()-1;j>=i;j--){
      if(r[j-1]>r[j]){
	int temp;
	temp=r[j-1];
	r[j-1]=r[j];
	r[j]=temp;
      }
    }
  }
    return r;
}
