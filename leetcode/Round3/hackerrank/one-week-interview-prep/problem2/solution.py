def plusMinus(arr):
    # Write your code here
    pos_count, neg_count, zero_count = 0,0,0 
    size = len(arr)
    for i in range(size):
        if(arr[i]>0):
            pos_count+=1
            continue
        if(arr[i]==0):
            zero_count+=1
            continue
        if(arr[i]< 0):
            neg_count+=1
            continue
    print(pos_count/size)
    print(neg_count/size)
    print(zero_count/size)