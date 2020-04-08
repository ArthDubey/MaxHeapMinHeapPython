from heapq import heappop,heappush,heapify
from MinHeapClass import Min_Heap
def randomArray(up):
    r=[random.randint(0,1000) for i in range(0,random.randint(5,up))]
    return r
    
def tests():
    t=input("Please enter the number of tests \nand len of array \nand inside tests:").split()
    t,up,inside_test=tuple(map(int,t))
    corr=0
    wrong=0
    for i in range(t):
        sample=randomArray(up)
        corheap=sample.copy()
        heapify(corheap)
        myheap=Min_Heap(sample)
        #print(corheap,myheap.h)
        for randos in range(inside_test):
            z=random.randint(1,2)
            if z==1:
                addmaal=random.randint(1,1000)
                #print("Adding ",addmaal)
                myheap.Add(addmaal)
                heappush(corheap,addmaal)
            if z==2 and len(corheap)>1:
                #print("Popping")
                MyRemoved=myheap.Minimum_pop()
                CorrectRemoved=heappop(corheap)
                if MyRemoved==CorrectRemoved:
                    #print("Right answer, Expected: ",CorrectRemoved,"Got: ",MyRemoved)
                    corr+=1
                else:
                    #print("Wrong answer, Expected: ",CorrectRemoved,"Got: ",MyRemoved)
                    wrong+=1
    print("Correct cases are:",corr,"Wrong cases are:",wrong,"Total cases are:",corr+wrong)
    print("Percentage stands at:",(corr/(corr+wrong))*100)
tests()
