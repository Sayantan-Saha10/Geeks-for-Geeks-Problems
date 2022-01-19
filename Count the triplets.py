"""

Count the triplets

Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Example 1:

Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 2
Explanation: There are 2 triplets: 
1 + 2 = 3 and 3 +2 = 5 

"""

""" My Solutions (Failed due to Time Complexity) """

def countTriplet(self, arr, n):
  i=0
  list_of_triplets = []
  while (i<n):
      j=0
      while (j<n):
          if ((i==j) or (arr[j] > arr[i])):
              j+=1
          else:
              d = arr[i] - arr[j]
              if (d in arr):
                  if (d != arr[j]):
                      list_of_triplets.append(tuple(sorted([arr[j],d])))
              j+=1
      i+=1
  return (len(set(list_of_triplets)))
  
  
  
def countTriplet(self, arr, n):
  i=0
  list_of_triplets = []
  while (i<n):
      j=0
      if not (arr[i] in [0, 1, 2]):
          while (j<n):
              if ((i==j) or (arr[j] > arr[i])):
                  j+=1
              else:
                  d = arr[i] - arr[j]
                  if (d in arr):
                      if (d != arr[j]):
                          list_of_triplets.append(tuple(sorted([arr[j],d])))
                  j+=1
      i+=1
  return (len(set(list_of_triplets)))
  
  

""" Online Solution """

def countTriplet(self, arr, n):
  i=0
  count = 0
  set_arr = set(arr)
  for i in range(n):
      for j in range(i+1, n):
          if ((arr[i]+arr[j]) in set_arr):
              count += 1

  return count
  
  
  
""" My Solution (Passed) """

def countTriplet(self, arr, n):
  i=0
  list_of_triplets = []
  set_arr = set(arr)
  while (i<n):
      j=0
      while (j<n):
          if ((i==j) or (arr[j] > arr[i])):
              j+=1
          else:
              d = arr[i] - arr[j]
              if (d in set_arr):
                  if (d != arr[j]):
                      list_of_triplets.append(tuple(sorted([arr[j],d])))
              j+=1
      i+=1
  return (len(set(list_of_triplets)))
  


""" Note - Time Complexity of List = O(N) and that of dict/set = O(1) """




