

def InsertionSort(ArrayToSort): 

      lenArray = len(ArrayToSort)
      Array = [ArrayToSort[0]]
      
      
      for Loop in range(1, lenArray, 1): 
            
            #Remove next line's comment to see how the array gets sorted
            #print("Sorting in progres... ", Array)
            
            CurrentNum = ArrayToSort[Loop]
            Array.append(None)
            
            # We set the new None where we want CurrentNum to be inserted
            Pivot = Loop
            while (Array[Pivot - 1] != None) and (Array[Pivot - 1] > CurrentNum): 
                  Array[Pivot] = Array[Pivot - 1]
                  Array[Pivot - 1] = None
                  Pivot = Pivot - 1
                  
                  if (Pivot == 0): 
                        break
                  #if
                  
            # While
            
            # We insert CurrentNum where None was placed
            Array[Pivot] = CurrentNum
            
      #for Loop in range
      
      #Our Array is sorted.
      return (Array)
#def InsertionSort

