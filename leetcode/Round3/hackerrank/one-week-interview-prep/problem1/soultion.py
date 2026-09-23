def countResponseTimeRegressions(responseTimes):
    # Write your code here
    if (len(responseTimes) < 2):
        return 0
    tSum = responseTimes[0]
    count = 0
    for idx,r in enumerate(responseTimes[1:]):
        avg = tSum / (idx + 1)
        if r > avg:
            count+=1
        tSum += r
    return count