#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Create:  2021/3/20 8:57
# Author: Baihao
#第二轮循环：从选择index后面一个元素至终点范围后与进行比较(此处优化为记录标志位，最后再替换)
#面试题：输出数组中两元素相加符合target的元素对

def select(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n): #第二轮循环：从选择index后面一个元素至终点范围后与进行比较(此处优化为记录标志位，最后再替换)
            minflag=i
            print(i,j)
            if arr[i] > arr[j]:
                minflag=j
                #arr[i],arr[j]=arr[j],arr[i]
            arr[i],arr[minflag] = arr[minflag],arr[i]
    return arr

def get_target(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                print(arr[i],arr[j])




if __name__ == '__main__':
    arr = [3,2,1,4]
    print(select(arr))
    get_target(arr,5)
