#!/usr/bin/python3

def pascal_helper(array, current, stop):
    if current == 1:
        array.append([1])
    elif current == 2:
        array.append([1, 1])
    else:
        last_arr = array[-1]
        last_len = len(last_arr)
        curr_arr = []
        i = 0;
        j = 1;
        curr_arr.append(1)
        while j < last_len:
            tmp = last_arr[i] + last_arr[j]
            i = j
            j+=1
            curr_arr.append(tmp)
        curr_arr.append(1)

        array.append(curr_arr)
    if current == stop:
        return
    else:
        return pascal_helper(array, current + 1, stop)
            

def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        arr = []
        pascal_helper(arr, 1, n);
        return arr
