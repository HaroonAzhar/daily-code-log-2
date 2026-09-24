def miniMaxSum(arr):
    # Write your code here
    n = len(arr)
    total = sum(arr)
    high = total - arr[0]
    low = total - arr[0]
    for i in range(1,n):
        curr = total - arr[i]
        high = max(high,curr)
        low = min(low,curr)
    print(f"{low} {high}")