from heapq import heappop,heappush,heapify # Testing the structure with in built
import random
class Min_Heap:
    def __init__(self,arr=[]):
        self.Heapify(arr)
        self.h=arr
        self.removed=set()
    def Heapify(self,arr):
        for i in range(len(arr)//2,-1,-1):
            self.NodeHeapifyDown(arr,i)
    def NodeHeapifyDown(self,arr,i=0):
        smallest=i
        if (2*i)+1<len(arr):
            if arr[(2*i)+1]<arr[i]:
                smallest=(2*i)+1
        if (2*i)+2<len(arr):
            if arr[(2*i)+2]<arr[smallest]:
                smallest=(2*i)+2
        if smallest!=i:   
            arr[i],arr[smallest]=arr[smallest],arr[i] 
            self.NodeHeapifyDown(arr,smallest)
        return
    def NodeHeapifyUp(self,arr,i):
        if i==0:
            return
        p=((i-1)//2)
        if arr[i]<arr[p]:
            arr[i],arr[p]=arr[p],arr[i]
            self.NodeHeapifyUp(arr,p)
        return
    def Add(self,val):
        self.h.append(val)
        self.NodeHeapifyUp(self.h,len(self.h)-1)
        return
    def Minimum_peek(self):
        if len(self.h)==0:  return -1
        return self.h[0]
    def Minimum_pop(self):
        if len(self.h)==0:  return -1
        self.h[0],self.h[-1]=self.h[-1],self.h[0]
        popped=self.h.pop()
        self.NodeHeapifyDown(self.h,0)
        return popped



