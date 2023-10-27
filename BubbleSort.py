
def BubbleSort(ArrayToSort): 
      
      Array = ArrayToSort.copy()
      
      #for Loop in range(1, len(Array), 1): 
      for Loop in range(len(Array) - 2, -1, -1):
            
            Key = Array[Loop]
            i = Loop + 1
            
            while (i < len(Array)) and (Array[i] < Key):
                  TempVar = Array[i - 1]
                  Array[i - 1] = Array[i]
                  Array[i] = TempVar
                  
                  i = i + 1
                  
            #while
            
      #for Loop in range
      
      return (Array)
#def BubbleSort

