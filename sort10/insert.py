#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Create:  2021/3/20 11:33
# refer to https://zhuanlan.zhihu.com/p/35328552
# Author: Baihao

# 基本思想
# 将一个数插入一个已经排好序的数据中。
# 第一次循环时，从第2个数开始处理。
# 我们将第1个数作为已经排好序的数据：当第2个数 > 第1个数时，将第2个数放在第1个数后面一个位置；
# 否则，将第2个数放在第1个数前面。此时，前两个数形成了一个有序的数据。
# 第二次循环时，我们处理第3个数。此时，前两个数形成了一个有序的数据：
# 首先比较第3个数和第2个数，当第3个数 > 第2个数时，将第3个数放在第2个数后面一个位置并结束此次循环；
# 否则，再和第1个数比较。如果第3个数 > 第1个数，则将第3个数插入第1个数和第2个数中间；
# 否则，第3个数 < 第1个数，则将第3个数放在第1个数前面。此时，前三个数形成了一个有序的数据。
# 后续的数据同理处理，直至结束。

def insert(arr):
    n = len(arr)
    if n <= 1:  #预检查
        return arr
    for i in range(1, n):
        #开始比较
        if arr[i] < arr[i - 1]:
            #临时变量存储key值
            temp = arr[i]
            #记录当前位置
            j = i
            #比temp大的数依次往后挪一个位置，为temp腾位置
            while j > 0 and temp < arr[j - 1]:
                arr[j] = arr[j - 1]
                j -= 1 #填充完毕后继续往前比较
            #将temp放在属于他的位置
            arr[j]=temp
    return arr


# 合并两个有序数组，并排序
# 每次比较两元素，比较后删除原数组中的元素
# 最后将剩余元素补足到列表中
# extend () 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。

def merge(l1, l2):
    res = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            res.append(l1[0])
            del l1[0]
        else:
            res.append(l2[0])
            del l2[0]
    res.extend(l1)
    res.extend(l2)
    return res


if __name__ == '__main__':
    arr = [5, 6, 3, 2, 4, 1]
    print(insert(arr))

    # l1 = [1,3,5]
    # l2 = [2,4,8,9]
    # print(merge(l1,l2))
    #
    # l1 = [1,3,5,6,7]
    # l2 = [2,4,8]
    # print(merge(l1,l2))
