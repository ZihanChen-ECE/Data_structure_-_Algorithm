#! /usr/bin/env
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Author: Zihan Chen
# Date: Jan 9th, 2017
#-------------------------------------------------------------------------------

import random


class BinarySearch(object):

# ------This part deals with two famous sorting method: quick sort and merge sort--------
    
    def QuickSort(self, nums):
        N = len(nums)
        if N <= 1:  return nums
        nums = self._quicksort(nums)
        return nums
    
    def _quicksort(self, nums):
        N = len(nums)
        if N <= 1:  return nums
        piv = nums[0]
        left = []
        right = []
        mid = []
        for ii in nums:
            if ii > piv:    right.append(ii)
            elif ii == piv: mid.append(ii)
            else:   left.append(ii)
        right = self._quicksort(right)
        left = self._quicksort(left)
        return left+mid+right

        
    def MergeSort(self, nums):
        N = len(nums)
        if N <= 1:  return nums
        nums = self._mergesort(nums)
        return nums
        
    def _mergesort(self, nums):
        N = len(nums)
        if N <= 1:  return nums
        left = []
        right = []
        mid = (N)//2
        left = self._mergesort(nums[:mid])
        right = self._mergesort(nums[mid:])
        return self.merge(left, right)                
        
    def merge(self, l1,l2):
        rList = list()
        N1 = len(l1)
        N2 = len(l2)
        ii = 0
        jj = 0
        while ii < N1 and jj < N2:
            if l1[ii] < l2[jj]:
                rList.append(l1[ii])
                ii+=1
            else:
                rList.append(l2[jj])
                jj+=1
        while ii < N1:
            rList.append(l1[ii])
            ii+=1
        while jj < N2:
            rList.append(l2[jj])
            jj+=1
        return rList


# ------------------------------Binary Search Starts from here-----------------------------    

    def BS1(self, nums, target):
        N = len(nums)
        if N == 0:  return -1

        left = 0
        right = N-1
        while right >= left :
            mid = (right+left)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                return mid
        # if nums[left] == target:
        #     return left
        # if nums[right] == target:
        #     return right
        return -1

        
    def BS2(self, nums, target):
        N = len(nums)
        if N == 0:  return -1

        left = 0
        right = N-1
        while right > left+1:
            mid = (right+left)//2
            if nums[mid]<target:
                left = mid
            elif nums[mid]>target:
                right = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1       

        
    def Sqrt(self, x):
        if x <= 3:  return 1
        right = x//2
        left = 1
        while right>left+1:
            mid = (right+left)//2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                left = mid
            else:
                right = mid
        if left**2 <= x and (left+1)**2 > x:    return left
        if right**2 <= x and (right+1)**2 > x:   return right                

    
    def RBS(self, nums, target):
        N = len(nums)
        if N == 0:  return -1

        left = 0
        right = N-1
        return self._RBS(nums, target, left, right)

        
    def _RBS(self, nums, target, left, right):
        if left+1 >= right:
            if nums[left] == target:    return left
            elif nums[right] ==  target:    return right
            else:   return -1
        mid = (left+right)//2
        if nums[mid] == target: right = mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid            
            
        return self._RBS(nums, target, left, right)


    def MatrixBS1(self, matrix, target):
        row = len(matrix)
        if row == 0:
            return -1
        col = len(matrix[0])
        if col == 0:    return -1
        left = 0
        right = row-1
        while left+1<right:
            mid = (left+right)//2
            if matrix[mid][0] == target:    return (mid,0)
            elif matrix[mid][0] < target:
                left = mid
            else:
                right = mid
        if matrix[right][0] <= target:
            row = right
        elif matrix[left][0] <= target:
            row = left
        else:
            return -1
        left = 0; right = col-1
        while left+1<right:
            mid = (left+right)//2
            if matrix[row][mid] == target:    return (row,mid)
            elif matrix[row][mid] < target:
                left = mid
            else:
                right = mid
        if matrix[row][right] == target:
            return (row, right)
        if matrix[row][left] == target:
            return (row, left)
        return -1
        
        
    def firstBadVersion(self, Versions):
        #This is iteration version
        N = len(Versions)
        if N == 0 or Versions[-1] != 'X':   return -1
        left = 0; right = N-1
        while left+1 < right:
            mid = (left+right)//2
            if Versions[mid] == 'X':
                right = mid
            elif Versions[mid] == 'O':
                left = mid
        if Versions[left] == 'X':   return left
        if Versions[right] == 'X':  return right
        return -1
    
    
    def RfirstBadVersion(self, Versions):
        #This is recursion version
        N = len(Versions)
        if N == 0 or Versions[-1] != 'X':   return -1
        left = 0; right = N-1
        return self._RFBV(Versions, left, right)
    
    def _RFBV(self, Versions, left, right):
        if left +1 >= right:
            if Versions[left] == 'X':   return left
            if Versions[right] == 'X':  return right
            return -1
        mid = (left+right)//2
        if Versions[mid] == 'X':
            right = mid
        else:
            left = mid
        return self._RFBV(Versions, left, right)
        
        
    def SearchRotatedArray(self, R_nums, target):
        # No repeating numbers in R_nums
        N = len(R_nums)
        if N == 0:  return -1
        left = 0; right = N-1
        while left+1 < right:
            mid = (left+right)//2
            if R_nums[mid] == target:
                return mid
            if R_nums[left] < R_nums[mid]:
                if R_nums[left] <= target and target <= R_nums[mod]:
                    right = mid
                else:
                    left = mid
            else:
                if R_nums[mid] <= target and target <= R_nums[right]:
                    left = mid
                else:
                    right = mid
                    
        if R_nums[left] == target:
            return left
        if R_nums[right] == target:
            return right
        return -1
      
        
    def RSearchRotatedArray(self, R_nums, target):
        # No repeating numbers in R_nums
        N = len(R_nums)
        if N == 0:  return -1
        left = 0; right = N-1
        return self._RSRA(R_nums, target, left, right)    
        
    def _RSRA(self, R_nums, target, left, right):
        if right < left + 1:
            if R_nums[left] == target:  return left
            if R_nums[right] ==  target:    return right
            return -1
            
        mid = (left + right)//2
        if R_nums[mid] == target:   return mid
        if R_nums[left] < R_nums[mid]:
            if R_nums[left] <= target and target <= R_nums[mid]:
                right = mid
            else:
                left = mid
        else:
            if R_nums[mid] <= target and target <= R_nums[right]:
                left = mid
            else:
                right = mid
                
        return self._RSRA(R_nums, target, left, right)
        
    
    def findMin_RotatedArray(self, R_nums):
        N = len(R_nums)
        if N < 1:  return -1
        left = 0; right = N-1
        while left+1<right:
            mid = (left+right)//2
            if R_nums[mid] >= R_nums[right]:
                left = mid
            else:
                right = mid
        if R_nums[left] < R_nums[right]:
            return R_nums[left], left
        else:
            return R_nums[right], right
        
        
    def findMax_RotatedArray(self, R_nums):
        N = len(R_nums)
        if N < 1:  return -1
        left = 0; right = N-1
        while left+1<right:
            mid = (left+right)//2
            if R_nums[mid] >= R_nums[left]:
                left = mid
            else:   right = mid
        if R_nums[left] >= R_nums[right]:
            return R_nums[left], left
        else:
            return R_nums[right], right
            
            
    def RfindMin(self, R_nums):
        N = len(R_nums)
        if N <= 1:  return -1
        left = 0; right = N-1
        return self._RFMin(R_nums, left, right)
        
    def _RFMin(self, R_nums, left, right):
        if right <= left+1:
            if R_nums[left] <= R_nums[right]:
                return R_nums[left], left
            else:
                return R_nums[right], right
        mid = (right+left)//2
        if R_nums[mid] >= R_nums[right]:
            left = mid
        else:
            right = mid
        return self._RFMin(R_nums, left, right)
        

    def RfindMax(self, R_nums):
        N = len(R_nums)
        if N <= 1:  return -1
        left = 0; right = N-1
        return self._RFMax(R_nums, left, right)
        
    def _RFMax(self, R_nums, left, right):
        if right <= left+1:
            if R_nums[left] >= R_nums[right]:
                return R_nums[left], left
            else:
                return R_nums[right], right
        mid = (right+left)//2
        if R_nums[mid] >= R_nums[left]:
            left = mid
        else:
            right = mid
        return self._RFMax(R_nums, left, right)
        
        
    def findPeakElement(self, nums):
        N = len(nums)
        if N < 2: return -1
        left = 1; right = N-2
        while left+1<right:
            mid = (left + right)//2
            if nums[mid] < nums[mid-1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid
        if nums[left] < nums[right]:
            return nums[right], right
        else:   return nums[left]. left
            
            
            
            
if __name__ == '__main__':
    nums = [1,2,5,6,6,6,6,6,8,9,17]
    random.shuffle(nums)
    print nums
    target = 6
    Solution = BinarySearch()
    print Solution._mergesort(nums)
    nums = Solution.QuickSort(nums)
    print nums
    random.shuffle(nums)
    print nums
    nums = Solution.MergeSort(nums)
    print nums
    print Solution.BS1(nums,target)
    print Solution.BS2(nums,target)
    print Solution.RBS(nums,target)
    print Solution.Sqrt(17)
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print matrix
    target = 5
    print Solution.MatrixBS1(matrix, target)
    
    versions = ['O','O','O', 'X','X','X']
    print Solution.firstBadVersion(versions)
    print Solution.RfirstBadVersion(versions)       
    
    # test the function for searching rotated sorted array
    print "{}".format("test the function for searching rotated sorted array")
    R_nums1 = [4,5,6,1,2,3]
    R_nums2 = [4,5,6,-2,-1,0,1,2,3]
    R_nums3 = [4,5,6,7,8,9,-2,0,1,2,3]
    target = -2
    print Solution.SearchRotatedArray(R_nums1, target)
    print Solution.SearchRotatedArray(R_nums2, target)
    print Solution.SearchRotatedArray(R_nums3, target)
    print Solution.RSearchRotatedArray(R_nums1, target)
    print Solution.RSearchRotatedArray(R_nums2, target)
    print Solution.RSearchRotatedArray(R_nums3, target)
    
    #test the function for searching the minimum value in a rotated sorted array
    print "{}".format("test the function for searching the minimum value in a rotated sorted array")
    print (Solution.findMin_RotatedArray(R_nums3)[0], Solution.findMin_RotatedArray(R_nums3)[1])
    print (Solution.RfindMin(R_nums3)[0], Solution.RfindMin(R_nums3)[1])
    
    
    #test the function for searching the maximum value in a rotated sorted array
    print "{}".format("test the function for searching the maximum value in a rotated sorted array")
    print (Solution.findMax_RotatedArray([4,5,6,0,1,2,3])[0], Solution.findMax_RotatedArray([4,5,6,0,1,2,3])[1])
    print (Solution.RfindMax([4,5,6,0,1,2,3])[0], Solution.RfindMax([4,5,6,0,1,2,3])[1])
    
    #test find peak (return any of the peak)
    nums = [1,10,1,3,4,7,1]
    print Solution.findPeakElement(nums)
    
    
    
    
    
    
    
    
    
    
    
    
     
            
            