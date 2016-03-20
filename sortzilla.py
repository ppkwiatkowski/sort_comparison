import numpy as np
import pylab as pl
import timeit,pdb,itertools,copy,pickle,sys,os

#pypyPath="/Users/pk/Downloads/pypy-4.0.1-src/"
#sys.path.append(os.path.normpath(pypyPath))
#sys.path.append(os.path.normpath(pypyPath+"/rpython/rlib"))

#from listsort import TimSort as TS

###############################################################
# Utility Functions
# (eg for feature extraction from sequences, timing, etc

def ExtractPairwiseFeatures(inSeq,numSamples=10):

    samples=[inSeq[int(tmp)] for tmp in pl.linspace(0,len(inSeq)-1,numSamples)]
    foo=[[cmp(samples[tmp1],samples[tmp2]) for tmp2 in range(tmp1+1,numSamples)]
         for tmp1 in range(numSamples)]
    return np.array(list(itertools.chain(*foo)))

def TimeAlgo(sortFunc,inSeq,numRounds=2):
    '''
    Time how long it takes to sort sequence "inSeq" using function "sortFunc"
    Run it <numRounds> times and take the average
    '''
    tmpFunc=lambda:sortFunc(copy.copy(inSeq))
    return timeit.timeit(tmpFunc,number=numRounds)/numRounds


######################################################
# Functions for generating test sequences
# Based on: http://warp.povusers.org/SortComparison/

def AlmostUp(n,percentRand=10):
    result=range(n)
    numRand=int((percentRand/100.0)*n)
    choices=iter(np.random.choice(range(n),numRand,replace=False))
    for count in range(int(numRand/2)):
        i1=choices.next()
        i2=choices.next()
        tmp=result[i1]
        result[i1]=result[i2]
        result[i2]=tmp
    return result

def AlmostDown(n,percentRand=10):
    result=AlmostUp(n,percentRand)
    result.reverse()
    return result

def CompleteRandom(n):
    return np.random.permutation(range(n)).tolist()

def RandomEnd(n,nRandom=256):
    result=np.array(range(n-nRandom))*2; # n sorted even numbers
    randInts=np.random.choice(result+1,nRandom,replace=False)
    return list(np.concatenate((result,randInts)))

seqGenerators=[CompleteRandom,AlmostUp,AlmostDown,RandomEnd]


###################################################################################################
# Sorting algorithms
# Some code borrowed from:
# https://www.daniweb.com/programming/software-development/code/216689/sorting-algorithms-in-python
#

def BubbleSort(arr):
    done = False
    while not done:
        done = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = False
    return arr

def QuickSortRecursive(arr,popInd=-1):
    a=list(arr)
    if len(a) <= 1: return a
    pivot = a.pop(popInd)
    before = [x for x in a if x <= pivot]
    after = [x for x in a if x > pivot]
    return QuickSort(before) + [pivot] + QuickSort(after)

# Merge sort
def MergeSort(list2,numIter=sys.maxint):
    iterCounter=itertools.count(0)
    return merge_sort_r(list2, 0, len(list2) -1,numIter,iterCounter)

# merge sort recursive (used by MergeSort)
def merge_sort_r(list2, first, last, numIter, iterCounter):
    if first < last:
        if iterCounter.next()>(numIter-1):
            return -1
        sred = (first + last)/2
        merge_sort_r(list2, first, sred,numIter,iterCounter)
        merge_sort_r(list2, sred + 1, last,10,itertools.count(0))
        merge(list2, first, last, sred)
    return 1

# merge (used by merge_sort_r)
def merge(list2, first, last, sred):
    helper_list = []
    i = first
    j = sred + 1
    while i <= sred and j <= last:
        if list2 [i] <= list2 [j]:
            helper_list.append(list2[i])
            i += 1
        else:
            helper_list.append(list2 [j])
            j += 1
    while i <= sred:
        helper_list.append(list2[i])
        i +=1
    while j <= last:
        helper_list.append(list2[j])
        j += 1
    for k in range(0, last - first + 1):
        list2[first + k] = helper_list [k]


# ShellSort
def ShellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

    
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

        
# Heap sort
def HeapSort(list2):
    first = 0
    last = len(list2) - 1
    create_heap(list2, first, last)
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]  # swap
        establish_heap_property (list2, first, i - 1)
# create heap (used by heap_sort)
def create_heap(list2, first, last):
    i = last/2
    while i >= first:
        establish_heap_property(list2, i, last)
        i -= 1
# establish heap property (used by create_heap)
def establish_heap_property(list2, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and list2[k] < list2[k + 1]:
            k += 1
        if list2[first] >= list2[k]:
            break
        list2[first], list2[k] = list2[k], list2[first]  # swap
        first = k
        

def QuickSort(list_,numIter=sys.maxint):
    """
    Iterative version of quick sort
    from: http://codexpi.com/quicksort-python-iterative-recursive-implementations/
    """

    left=0
    right=len(list_)-1
    temp_stack = []
    temp_stack.append((left,right))
    
    #Main loop to pop and push items until stack is empty
    iterCounter=itertools.count()
    while temp_stack:      
        if iterCounter.next()>(numIter-1):
            return -1
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        #piv = partition_randomized(list_,left,right)
        piv = partition(list_,left,right)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            temp_stack.append((piv+1,right))
    return 1
  
def partition(list_, left, right):
    """
    Partition method
    """
    #Pivot first element in the array
    piv = list_[left]
    i = left + 1
    j = right
 
    while 1:
        while i <= j  and list_[i] <= piv:
            i +=1
        while j >= i and list_[j] >= piv:
            j -=1
        if j <= i:
            break
        #Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    #Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j

def partition_randomized(list_, left, right,piv=-1):
     """
     Partition method
     but choses random pivot
     """

     #Pivot random element in the array
     if piv==-1: piv = list_[np.random.randint(left,right+1)]
     i = left
     j = right
     
     while 1:
        while i <= j  and list_[i] < piv:
             i +=1
        while j >= i and list_[j] > piv:
            j -=1
        if j <= i:
            break
        #Exchange items
        list_[i], list_[j] = list_[j], list_[i]
     return j

# Decision Tree Sort! ;-)
def DTSort(inSeq,dt=-1,numSamples=-1,verbose=False):

    if dt==-1:
        dt=pickle.load(open('dtsorttree.pkl'))
    if numSamples==-1:
        numSamples=int(((1+8*(dt.n_features_))**0.5+1)/2.0)

    pred=dt.predict(ExtractPairwiseFeatures(inSeq,numSamples))
    tmpFunc={1:MergeSort,-1:QuickSort}[pred[0]]

    if verbose:
        print "Using "+tmpFunc.func_name

    tmpFunc(inSeq)


# QuickMerge Sort ;-);-)
def QuickMergeSort(inSeq,numMerge=5):
    MergeSort(inSeq,numIter=numMerge)
    QuickSort(inSeq)

def MergeQuickSort(inSeq,numQuick=5):
    QuickSort(inSeq,numIter=numQuick)
    MergeSort(inSeq)

def RandQuickSort(list_,numIter=sys.maxint):
    np.random.shuffle(list_)
    left=0
    right=len(list_)-1
    temp_stack = []
    temp_stack.append((left,right))
    
    #Main loop to pop and push items until stack is empty
    iterCounter=itertools.count()
    while temp_stack:      
        if iterCounter.next()>(numIter-1):
            return -1
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_,left,right)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            temp_stack.append((piv+1,right))
    return 1

# inSeq must be list!
#def TimSort(inSeq):
#    TS(inSeq).sort()   
  

sortAlgos=[ShellSort,HeapSort,MergeSort,QuickSort] #,TimSort]

############################################3
# Functions for plotting
#

# Plot the bar charts like in the povusers study
# Based on http://matplotlib.org/examples/pylab_examples/barchart_demo.html
def PlotCompBar(result,algoNames,seqNames,plotTitle='',spacer=1.5,barWidth=0.25,loc=2):
    n_groups = len(result[0])
    index = np.arange(n_groups)*spacer+0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    
    pl.hold('on')

    bariter=iter(xrange(10))
    labeliter=iter(seqNames)
    coloriter=iter(['r','g','b','m','y'])
    
    for res in result:
        rects1 = pl.bar(index+barWidth*bariter.next(), res, barWidth,alpha=opacity,color=coloriter.next(),label=labeliter.next())
    
    pl.xticks(rotation=45)
    pl.xlabel('Algorithm')
    pl.ylabel('Time(s)')
    pl.title(plotTitle)
    pl.xticks(index + barWidth, algoNames)
    pl.legend(loc=loc)
    pl.plot(0,0,'w.')
    pl.tight_layout()
    pl.show()


# Plot the time traces
def PlotAlgoTimes(result,algoNames,xValues=[],xLabel="",yLabel="",plotTitle="",newFig=True,loc=2):
    
    if newFig:
        pl.figure()

    pl.hold('on')
    if xValues==[]:
        xValues=range(len(result))
    labeliter=iter(['r-', 'g-', 'b-', 'c-', 'm-', 'y-', 'k-',
                    'r--', 'g--', 'b--', 'c--', 'm--', 'y--', 'k--',
                    'r:', 'g:', 'b:', 'c:', 'm:', 'y:', 'k:'])
    for res in result:
        pl.plot(xValues,res,labeliter.next())
    pl.legend(algoNames,loc=loc)
    pl.axis('tight')
    pl.title(plotTitle)
    pl.xlabel(xLabel)
    pl.ylabel(yLabel)
    pl.show()
