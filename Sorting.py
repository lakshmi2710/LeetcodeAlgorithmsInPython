class sorting:
        def Selectionsorting(self, Array):
            for i in range(len(Array)):
                minIndex = i
                for j in range(len(Array)):
                    if Array[j] < Array[minIndex]:
                        minIndex = j
                if i != minIndex:
                    sorting.swap(Array,i,minIndex)

        def swap(self, Array, i ,j):
             temp = Array[i]
             Array[i]  = Array[j]
             Array[j] = temp

        def bubbleSOrt(self, Array):
            lenOfArray = len(Array)

            for i in range(lenOfArray):
                for j in range(lenOfArray - 1):
                    if Array[j] > Array[j + 1]:
                        sorting.swap(Array, j, j + 1)



if __name__ == '__main__':
    Array = [3,1,2,4,5]
    print Array
    Sort =sorting
    Sort.Selectionsorting(Array)