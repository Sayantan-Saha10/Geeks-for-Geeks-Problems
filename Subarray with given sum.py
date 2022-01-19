"""
Subarray with given sum

Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

"""



""" My Solutions (Failed due to Time Complexity)"""

def subArraySum(self,arr, n, s): 
  i=0
  while (i<len(arr)):
      sum_value=0
      j=i
      while (sum_value<s):
          sum_value += arr[j]
          j += 1
      if (sum_value == s):
          return (str(i) + str(j))
      else:
          i += 1
          
         
""" Online Solution """

def subArraySum(self,arr, n, s):
  sum_value = 0
  i,j = 0,0
  while (j<n):
      sum_value += arr[j]
      if (sum_value < s):
          j+=1
      elif (sum_value == s):
          return [i+1, j+1]
      else:
          while (sum_value > s):
              sum_value -= arr[i]
              i += 1
          if (sum_value == s):
              return [i+1, j+1]
          j += 1
  return [-1]
