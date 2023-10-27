from pylab import *                    #Necesarry to generate random values
from time import perf_counter    #Necesarry to precisely time the execution
import matplotlib.pyplot as plt     #Necesarry to graph the final result
import matplotlib.patches as mpatches #Also for the graph

#Importing annex files
import InsertionSort
import MergeSort
import BubbleSort
import QuickSort





#We start with an empty array
Array = [] 

#Define how many measurments we want
#Default: 500
Start = 1 
End = 500
Increment = 1

# Defines automatically how many iterations will be ran
# from the Start / End / Interations we chose above
Iterations = round( (End-Start) / Increment)
intInterations = int(Iterations)


#Creation of arrays that will save the times it took to execute each sort
TimeInsertionSort = []
TimeBubbleSort =[]
TimeMergeSort = []
TimeQuickSort = []

#Start of the test:
for Loop in range(Start, End, Increment): 
      
      #We insert a random value into our array to sort
      #This allows for a random array generated. Not the best nor worst
      #cases of each sorting alg, but a realistic case.
      Array.append(randint(0, 10000))
      
      
      #Times of the Insertion Sort: 
      TimeStart = perf_counter()
      
      SortedArray = InsertionSort.InsertionSort(Array)
      
      TimeFinish = perf_counter()
      FinalTime = TimeFinish - TimeStart
      TimeInsertionSort.append(FinalTime)
      
      
      
      
      #Times of the Bubble Sort: 
      TimeStart = perf_counter()
      
      SortedArray = BubbleSort.BubbleSort(Array)
      
      TimeFinish = perf_counter()
      FinalTime = TimeFinish - TimeStart
      TimeBubbleSort.append(FinalTime)
      
      
      
      
      #Times of the Merge Sort: 
      TimeStart = perf_counter()
      
      SortedArray = MergeSort.MergeSort(Array)
      
      TimeFinish = perf_counter()
      FinalTime = TimeFinish - TimeStart
      TimeMergeSort.append(FinalTime)
      
      
      
      
      #Times of the Quick Sort: 
      TimeStart = perf_counter()
      
      SortedArray = QuickSort.QuickSort(Array)
      
      TimeFinish = perf_counter()
      FinalTime = TimeFinish - TimeStart
      TimeQuickSort.append(FinalTime)
      
#For Loop in Range


#Defining the x axis of the graph
x = [] 
for Loop in range(intInterations):
      x.append(Loop + 1)
#for loop in range



#Plotting the graph

fig, ax = plt.subplots()
Red = mpatches.Patch(color='red', label='Insertion Sort')
Magenta = mpatches.Patch(color='magenta', label='Bubble Sort')
Blue = mpatches.Patch(color='blue', label='Merge Sort')
Green = mpatches.Patch(color='green', label='Quick Sort')

ax.legend(handles=[Red, Magenta, Blue, Green])




plt.title("Time comparaison of different sorting algs")

plt.scatter(x, TimeInsertionSort, s=15, c='red')   #Plotting the InsertionSort
plt.scatter(x, TimeBubbleSort, s=15, c='m')   #Plotting the BubbleSort
plt.scatter(x, TimeMergeSort, s=15, c='blue')   #Plotting the MergeSort
plt.scatter(x, TimeQuickSort, s=15, c='green')   #Plotting the QuickSort

plt.xlabel("Number of elements in the array")
plt.ylabel("Time in seconds to sort the array")




plt.show()


