#include<iostream>
#include<vector>
#include "sorting.h"
using namespace std;

//update
vector<int> merge(vector<int> left, vector<int> right)
{
   vector<int> result;
   while ((int)left.size() > 0 || (int)right.size() > 0) {
      if ((int)left.size() > 0 && (int)right.size() > 0) {
         if ((int)left.front() <= (int)right.front()) {
            result.push_back((int)left.front());
            left.erase(left.begin());
         } 
   else {
            result.push_back((int)right.front());
            right.erase(right.begin());
         }
      }  else if ((int)left.size() > 0) {
            for (int i = 0; i < (int)left.size(); i++)
               result.push_back(left[i]);
            break;
      }  else if ((int)right.size() > 0) {
            for (int i = 0; i < (int)right.size(); i++)
               result.push_back(right[i]);
            break;
      }
   }
   return result;
}

vector<int> sort_custom(vector<int> m)
{
   if (m.size() <= 1)
      return m;
 
   vector<int> left, right, result;
   int middle = ((int)m.size()+ 1) / 2;
 
   for (int i = 0; i < middle; i++) {
      left.push_back(m[i]);
   }

   for (int i = middle; i < (int)m.size(); i++) {
      right.push_back(m[i]);
   }
 
   left = sort_custom(left);
   right = sort_custom(right);
   result = merge(left, right);
 
   return result;
}
