
#Setting up the parameters
def MergeSort(ArrayToSort): 

      Array = ArrayToSort.copy()
      SortedArray = MergeSortAlg(Array)
      return (SortedArray)
# Def Merge Sort


def MergeSortAlg(Array):
      
      
      if (len(Array) > 1):
            
            #Separate the original array
            r = len(Array) // 2 #Find where to split Array
            M = Array[r:] #M = From r to where the array finishes
            L = Array[:r] #L = From start of the array until r
            
            
            MergeSortAlg(L)
            MergeSortAlg(M)
            
            
            #Sorting until L or M is left empty
            PositionL = 0 # L[i]
            PositionM = 0 # M[j]
            PositionArray = 0 # Array[PositionArray ]
            
            
            while (PositionL < len(L)) and (PositionM < len(M)):
                     
                     if (L[PositionL] < M[PositionM]):
                           Array[PositionArray] = L[PositionL]
                           PositionL = PositionL + 1
                     # if
                     
                     else: 
                           Array[PositionArray] = M[PositionM]
                           PositionM = PositionM + 1
                     #Else
                     
                     PositionArray = PositionArray + 1
            #While
            
            
            
            #Add the leftover values to the array
            while (PositionL < len(L)):
                  Array[PositionArray] = L[PositionL]
                  PositionArray = PositionArray + 1
                  PositionL = PositionL + 1
            # While PositionL < len(L)
            
            while (PositionM < len(M)):
                  Array[PositionArray] = M[PositionM]
                  PositionArray = PositionArray + 1
                  PositionM = PositionM + 1
            # While PositionL < len(L)
            
      #if (len(Array) > 1)
      
      return(Array)
#def MergeSortAlg


