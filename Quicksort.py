import random
import sys  # 导入sys模块
sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000
""" import time

def cal_time(func):
	def wraper(*args,**kwargs):
		t1 = time.time()
		result = func(*args,**kwargs)
		t2 = time.time()
		print('%s running time %s　second' % (func.__name__, t2-t1))
		return result
	return wraper
 """
def partition (li ,left,right):
    temp = li[left]
    while left < right:
        while li[right] >= temp and left < right:
            right -=1   #左走一步
        li[left] = li[right]
        while li[left] <= temp and left < right:
            left +=1
        li[right] = li[left]
    li[left] = temp
    return left

def _quicksort(li , left ,right):
    if left < right:
        mid=partition(li,left,right)
        _quicksort(li, left ,mid-1)
        _quicksort(li, mid+1, right)
# @cal_time
def quicksort( li):
    _quicksort(li,0,len(li)-1)

#li=[9,4,5,7,3,45,67,3,4,56]

li = list( range((1000)))

quicksort(li)

print(li)
