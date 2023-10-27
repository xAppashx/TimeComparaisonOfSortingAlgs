The goal of the project is to demonstrate the different efficiencies of various sorting algorithms. 

  The file "TimeComparison" tests 4 sorting algorithms: Insertion Sort, Bubble Sort, Merge Sort, and Quick Sort. These 4 algorithms are in annex files of the project. 

  To test the efficiency of each sorting algorithm, we generate an array with a controlled length, but the values inside of the array are generated randomly, hence, not sorted. The reasoning behind it is to control how long it takes for each sorting algorithm to sort an array of length n, whilst creating a “realistic” scenario of sorting (not the best nor worst efficiency case of each sorting algorithm). 

  Inside of a loop, we send to each sorting algorithm the exact same array to sort, and we evaluate how much time each algorithm took to return us the sorted array. We repeat this process, each time with an array of n + 1 length. This allows us, with a loop sufficently high, to see a patern and to determine which algorithm in between these 4 is the fastest with increasingly long arrays. 
This also allows us to put a guess on the Big O efficiency of each of those 4 sorting algorithms. 

  After running the code “TimeComparison”, we obtain the graph called “Result1” in annex files. 
We can see 2 groups form: The Insertion and Bubble sort seem to perform approximately the same. Then we have the Merge and Quick sort: they perform similarly to each other, but that are significantly faster than the Insertion and Bubble sort at high n values.  

  The annex file “Result2” is a closeup of the Merge and Quick sort. Focusing only on these 2 by not plotting the Insertion and Bubble sort (comment out the lines 117 and 118), we start to see a difference in between these 2 algorithms. The Quick sort (like its name indicates) turns out to be the quickest here. 
  
  But does that make it the fastest sorting algorithm there is?
Find out in my future repositories!

