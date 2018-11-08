def selsort(arr):
    
    for outindex in range(len(arr)):
    
        for index in range(outindex, len(arr)):
            if index == 0:
                tmp = arr[index]
            else:
                if(tmp > arr[index]):
                    tmp = arr[index]
        #print("before", arr[outindex], "  ",outindex,"   ", tmp, " ", arr)
        if(arr[outindex] > tmp):
            
            tmpindex = arr.index(tmp)
            swap = arr[tmpindex]
            arr[tmpindex] = arr[outindex]
            arr[outindex] = swap
        #print("after", arr[outindex], "  ",outindex,"   ", tmp, " ", arr)
        tmp =arr[index]
    
    print(arr)
            

arr = [2, 11, 5, 6, 3, 4, 9, 8, 1, 7, 10]
state = selsort(arr)